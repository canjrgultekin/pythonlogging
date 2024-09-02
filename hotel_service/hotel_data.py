from common.database import Database

db = Database('hotel_service.db')

def create_hotel_table():
    db.execute('''CREATE TABLE IF NOT EXISTS hotels (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    location TEXT NOT NULL
                  )''')

def add_hotel(name, location):
    db.execute("INSERT INTO hotels (name, location) VALUES (?, ?)", (name, location))

def get_all_hotels():
    db.execute("SELECT * FROM hotels")
    return db.fetchall()
