import sqlite3

CONN = sqlite3.connect('library_data.db')
CURSOR = CONN.cursor()
