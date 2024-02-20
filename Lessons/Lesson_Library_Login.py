import sqlite3
from passlib.hash import sha256_crypt

hasher = sha256_crypt.using(rounds=30000)

def make_hash(text: str):
    return hasher.hash(text)

def check_hash(text: str, hashed: str):
    return hasher.verify(text, hashed)
class DatabaseWorker:
    def __init__(self, name):
        self.name_db = name
        self.connection = sqlite3.connect(self.name_db)
        self.cursor = self.connection.cursor()

    def run_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def insert(self, query):
        self.run_query(query)

    def search(self, query, multiple=False):
        results = self.cursor.execute(query)
        if multiple:
            return results.fetchall()
        return results.fetchone()
    def create(self):
        query = """CREATE TABLE IF NOT EXISTS Words(
                    id INTEGER PRIMARY KEY,
                    text TEXT NOT NULL unique,
                    length INTEGER NOT NULL
                    )"""
        self.run_query(query)

    def close(self):
        self.connection.close()