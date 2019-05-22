import sqlite3

conn = sqlite3.connect('entries.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE entries (date text, entry text)""")

conn.commit()
conn.close()
