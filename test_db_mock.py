import pytest
import unittest.mock as mock
import simple_db
import sqlite3

@mock.patch('sqlite3.connect')
def test_update_director(mock_dir):
    mock_resp = mock.Mock()
    mock_resp.return_value = [('Avengers', 'Joe Russo', '20/11/2010')]
    mock_dir.return_value = mock_resp
    simple_db.update_director('Mark Russo', 'Joe Russo')
    exp_data = simple_db.select_all_movies('Joe Russo')
    print(exp_data)
    assert exp_data == [('Avengers', 'Joe Russo', '20/11/2010')]

