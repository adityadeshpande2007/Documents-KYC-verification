import sqlite3

def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kyc (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        dob TEXT,
        address TEXT,
        id_number TEXT
    )
    """)
    
    conn.commit()
    conn.close()

def save_data(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    INSERT INTO kyc (name, dob, address, id_number)
    VALUES (?, ?, ?, ?)
    """, (data['name'], data['date_of_birth'], data['address'], data['id_number']))
    
    conn.commit()
    conn.close()