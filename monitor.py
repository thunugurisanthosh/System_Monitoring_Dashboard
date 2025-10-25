
import psutil
import sqlite3
from datetime import datetime

conn = sqlite3.connect('system_metrics.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS metrics (
             timestamp TEXT, cpu REAL, memory REAL, disk REAL)''')

cpu = psutil.cpu_percent()
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

c.execute("INSERT INTO metrics VALUES (?, ?, ?, ?)", (timestamp, cpu, memory, disk))
conn.commit()
conn.close()
print(f"Metrics saved at {timestamp}")
