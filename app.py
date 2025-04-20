from flask import Flask, render_template, request, jsonify
import sqlite3
import random
from datetime import datetime

app = Flask(__name__)

# Quotes for each mood
quotes = {
    "happy": [
        "Happiness is not by chance, but by choice.",
        "Smile, it's free therapy!",
        "The purpose of our lives is to be happy."
    ],
    "sad": [
        "Tough times never last, but tough people do.",
        "It's okay to not be okay.",
        "Stars can’t shine without darkness."
    ],
    "angry": [
        "For every minute you remain angry, you give up sixty seconds of peace of mind.",
        "Take a deep breath. You got this.",
        "Anger is one letter short of danger."
    ],
    "motivated": [
        "Don't watch the clock; do what it does. Keep going.",
        "Push yourself, because no one else is going to do it for you.",
        "The harder you work for something, the greater you'll feel when you achieve it."
    ],
    "bored": [
        "Boredom: the desire for desires.",
        "Try something new. Maybe a book or a walk?",
        "Creativity often comes from boredom!"
    ]
}

# Initialize database
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mood_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mood TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

# Log mood and timestamp
def log_mood(mood):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO mood_logs (mood, timestamp) VALUES (?, ?)", (mood, datetime.now()))
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_quote', methods=['POST'])
def get_quote():
    data = request.get_json()
    mood = data.get("mood")
    quote = random.choice(quotes.get(mood, ["Sorry, I don't have quotes for that mood."]))
    log_mood(mood)
    return jsonify({"quote": quote})

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5520)
