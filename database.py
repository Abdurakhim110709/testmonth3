import sqlite3

class Database:
    def __init__(self, path):
        self.path = path


    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS complaints(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    inst TEXT,
                    review TEXT
                )""")
            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)
            conn.commit()

    def fetch(self, query: str, params: tuple = None):
        with (sqlite3.connect(self.path) as conn):
            result = conn.execute(query, params)
            result.row_factory = sqlite3.Row
            data = result.fetchall()
            return [dict(r) for r in data]
