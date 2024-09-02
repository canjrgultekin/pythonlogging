from common.database import Database

db = Database('reservation_service.db')

def create_reservation_table():
    db.execute('''CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    hotel_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    FOREIGN KEY(user_id) REFERENCES users(id),
                    FOREIGN KEY(hotel_id) REFERENCES hotels(id)
                  )''')

def add_reservation(user_id, hotel_id, date):
    db.execute("INSERT INTO reservations (user_id, hotel_id, date) VALUES (?, ?, ?)", (user_id, hotel_id, date))

def get_all_reservations():
    db.execute("SELECT * FROM reservations")
    return db.fetchall()
