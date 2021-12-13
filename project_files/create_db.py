import sqlite3
import os

db = \
"""
PRAGMA foreign_keys=ON;
BEGIN TRANSACTION;
CREATE TABLE Recipes (recipe_id INTEGER PRIMARY KEY, name TEXT, url TEXT, user_id INTEGER, FOREIGN KEY (user_id) REFERENCES Users (user_id));
CREATE TABLE Users (user_id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT);
COMMIT;
"""

if os.path.exists('db.sqlite'):
	print('db.sqlite already exists')
else:
	conn = sqlite3.connect('db.sqlite')
	conn.cursor().executescript(db)
	conn.commit()
