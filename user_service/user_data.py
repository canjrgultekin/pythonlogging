from common.database import Database

db = Database('user_service.db')

def create_user_table():
    db.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL
                  )''')

def register_user(username, password):
    try:
        db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        return True
    except:
        return False

def validate_user(username, password):
    db.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return db.fetchone()
