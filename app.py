
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def dashboard():
    conn = sqlite3.connect('system_metrics.db')
    c = conn.cursor()
    c.execute("SELECT * FROM metrics ORDER BY timestamp DESC LIMIT 10")
    data = c.fetchall()
    conn.close()
    return render_template('dashboard.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
