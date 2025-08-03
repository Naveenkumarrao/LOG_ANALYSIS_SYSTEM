import pandas as pd
import mysql.connector
from datetime import datetime

# Load cleaned logs
df = pd.read_csv("cleaned_logs.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="log_analysis"
)
cursor = conn.cursor()

for _, row in df.iterrows():
    try:
        # Parse datetime
        dt = datetime.strptime(row['datetime'], '%d/%b/%Y:%H:%M:%S %z')

        # Insert into log_entries
        cursor.execute("""
            INSERT INTO log_entries (ip, datetime, method, endpoint, protocol, status_code, size)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            row['ip'], dt, row['method'], row['endpoint'],
            row['protocol'], int(row['status_code']), int(row['size'])
        ))

        log_id = cursor.lastrowid

        # Insert into user_agents
        cursor.execute("""
            INSERT INTO user_agents (log_entry_id, user_agent)
            VALUES (%s, %s)
        """, (log_id, row['user_agent']))

    except Exception as e:
        print(f"⚠️ Skipping row due to error: {e}")

conn.commit()
cursor.close()
conn.close()

print("✅ All cleaned logs inserted into database.")
