import unittest
import os
import simple_db
import sqlite3


class TestMovieDatabase(unittest.TestCase):

    def setUp(self) -> None:
        
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE movies
                    (title text, director text, release_date text)
                    """)
        
        cursor.execute("INSERT INTO movies VALUES"
                    "('Avengers', 'Mark Russo', '20/11/2010')")
        
        conn.commit()

        movies = [('Endgame', 'Russo Brothers', '1/4/2020'),
                ('The Social Network', 'Steven Spielberg', '2/3/2009'),
                ('Spiderman', 'Stan Lee', '1/2/2002'),
                ('Ironman', 'Fat Man', '2/3/2008')]
        
        cursor.executemany("INSERT INTO movies VALUES (?, ?, ?)", movies)
        conn.commit()
        cursor.close()
        conn.close()


    def tearDown(self) -> None:
        os.remove('mydatabase.db')

    
    def test_updating_director(self):
        simple_db.update_director('Mark Russo', 'Joe Russo')
        actual = simple_db.select_all_movies('Joe Russo')
        expected = [('Avengers', 'Joe Russo', '20/11/2010')]
        assert actual == expected

    def test_director_non_existent(self):
        result = simple_db.select_all_movies('Meeka')
        self.assertFalse(result)