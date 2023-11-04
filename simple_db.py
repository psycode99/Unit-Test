import sqlite3

def create_databse():
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


def delete_director(director):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    sql = """
    DELETE FROM movies
    WHERE director = ?
    """

    cursor.execute(sql, [(director)])
    conn.commit()
    cursor.close()
    conn.close()

def update_director(director, new_director):

    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    sql = """
    UPDATE movies
    SET director = ?
    WHERE director = ?
    """

    cursor.execute(sql, (new_director, director))
    conn.commit()
    cursor.close()
    conn.close()


def select_all_movies(director):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    sql = """
    SELECT * FROM movies
    WHERE director = ?
    """

    cursor.execute(sql, [(director)])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


if __name__ == '__main__':
    import os
    if not os.path.exists('mydatabase.db'):
        create_databse()
    
    delete_director('Fat Man')
    update_director('Stan Lee', 'Alfred Hitchcock')
    print(select_all_movies('Mark Russo'))

