import sqlite3

db_name = "passwords.db"

def create_database():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS passwords(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   service TEXT NOT NULL,
                   username TEXT NOT NULL,
                   password TEXT NOT NULL)""")
    conn.commit()
    conn.close()

def save_password(service, username, password):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (service, username, password) VALUES (?,?,?)", 
                   (service, username, password))
    conn.commit()
    conn.close()

def get_password(service, username, password):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM passwords WHERE service=?", (service,))
    result = cursor.fetchone()
    conn.close()
    return result

