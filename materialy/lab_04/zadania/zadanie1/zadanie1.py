import requests
import sqlite3

response = requests.get("https://randomuser.me/api/?results=30")
users = response.json()["results"]

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# 2. Stworz tabele Users (id, first_name, last_name, email, age, gender, country)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    country TEXT NOT NULL          
    )
''')

for user in users:
    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    email = user["email"]
    age = user["dob"]["age"]
    gender = user["gender"]
    country = user["location"]["country"]

    cursor.execute("INSERT INTO users (first_name, last_name, email, age, gender, country) VALUES (?, ?, ?, ?, ?, ?)", (first_name, last_name, email, age, gender, country))

conn.commit()


print(f"\n {cursor.execute('SELECT gender, COUNT(*) FROM users GROUP BY gender').fetchall()}")
print("=====================================================================================")
print(f"\n {cursor.execute('SELECT AVG(age) FROM Users').fetchall()}")
print("=====================================================================================")
print(f"\n {cursor.execute('SELECT country, COUNT(*) FROM Users GROUP BY country ORDER BY COUNT(*) DESC').fetchall()}")

conn.close()

