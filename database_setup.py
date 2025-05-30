import sqlite3
import requests
import json


conn = sqlite3.connect("weather_data.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS weather")

cursor.execute("""
               CREATE TABLE IF NOT EXISTS weather (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               city TEXT,
               temparature REAL,
               humidity INTEGER,
               description TEXT,
               timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
               )
               """)
conn.commit()