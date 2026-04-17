from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Database Setup
def init_db():
    conn = sqlite3.connect('database.db')
    db = conn.cursor()
    db.execute('CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, item TEXT, count INTEGER)')
    # Insert a sample record if empty
    db.execute('SELECT COUNT(*) FROM inventory')
    if db.fetchone()[0] == 0:
        db.execute("INSERT INTO inventory (item, count) VALUES ('Cloud Servers', 50)")
        conn.commit()
    conn.close()

init_db()

@app.route("/api/inventory")
def get_inventory():
    conn = sqlite3.connect('database.db')
    db = conn.cursor()
    db.execute("SELECT item, count FROM inventory")
    item, count = db.fetchone()
    conn.close()
    
    return jsonify({
        "architecture": "Three-Tier",
        "item_name": item,
        "quantity": count,
        "db_type": "SQLite"
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001) # Using 5001 to avoid conflict
