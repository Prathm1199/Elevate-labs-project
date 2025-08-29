import sqlite3
import time

# Initialize database
conn = sqlite3.connect('packets.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS packets
             (timestamp REAL, src_ip TEXT, dst_ip TEXT, src_port INT, dst_port INT, proto TEXT)''')
conn.commit()

def log_packet(packet_info):
    timestamp, src_ip, dst_ip, src_port, dst_port, proto = packet_info
    c.execute("INSERT INTO packets VALUES (?, ?, ?, ?, ?, ?)",
              (timestamp, src_ip, dst_ip, src_port, dst_port, proto))
    conn.commit()

def get_summary():
    c.execute("SELECT src_ip, COUNT(*) FROM packets GROUP BY src_ip")
    return c.fetchall()
