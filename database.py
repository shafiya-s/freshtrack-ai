import sqlite3

DB_NAME = "freshtrack.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_tables():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        quantity INTEGER,
        unit TEXT,
        purchase_date TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS shelf_life (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT UNIQUE,
        shelf_life_days INTEGER,
        photo_supported INTEGER
    )
    """)

    conn.commit()
    conn.close()


def seed_shelf_life():
    items = [
        ("Banana", 5, 0),
        ("Tomato", 7, 0),
        ("Coriander", 3, 0),
        ("Mango", 6, 0),
        ("Strawberry", 4, 0),
        ("Avocado", 5, 0),
        ("Grapes", 7, 0),
        ("Cucumber", 7, 0),
        ("Green Chilli", 10, 0),
        ("Lemon", 14, 0)
    ]

    conn = get_connection()
    c = conn.cursor()

    for item in items:
        c.execute("""
        INSERT OR IGNORE INTO shelf_life
        (item_name, shelf_life_days, photo_supported)
        VALUES (?, ?, ?)
        """, item)

    conn.commit()
    conn.close()


create_tables()
seed_shelf_life()