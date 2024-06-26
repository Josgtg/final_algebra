import sqlite3
from classes import Comida
import os
import table

if not os.path.exists("db/"):
    os.makedirs("db")

if not os.path.exists("db/algebra.db"):
    open("db/algebra.db", "w").close()

conn = sqlite3.connect("db/algebra.db")
cur = conn.cursor()

def create_table():
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='comidas';")

    if cur.fetchall():
        return

    cur.execute(f" CREATE TABLE {table.name} ({table.schema});")

    cur.executemany(table.insert, table.data)

    conn.commit()


def get_datos() -> list[Comida]:
    cur.execute(f"SELECT * FROM {table.name};")
    return [Comida(i) for i in cur.fetchall()]

def close():
    conn.close()