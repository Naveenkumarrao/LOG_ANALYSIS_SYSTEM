import mysql.connector
from tabulate import tabulate

class MySQLHandler:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        with open('create_tables.sql', 'r') as f:
            sql = f.read()
        for statement in sql.split(';'):
            if statement.strip():
                self.cursor.execute(statement)
        self.conn.commit()

    def get_top_n_endpoints(self, n=10):
        self.cursor.execute("""
            SELECT endpoint, COUNT(*) AS request_count
            FROM logs
            GROUP BY endpoint
            ORDER BY request_count DESC
            LIMIT %s
        """, (n,))
        return self.cursor.fetchall()

    def get_status_code_distribution(self):
        self.cursor.execute("""
            SELECT status_code, COUNT(*) AS count
            FROM logs
            GROUP BY status_code
            ORDER BY count DESC
        """)
        return self.cursor.fetchall()

    def get_error_rate(self):
        self.cursor.execute("""
            SELECT 
                ROUND(100.0 * SUM(CASE WHEN status_code >= 400 THEN 1 ELSE 0 END) / COUNT(*), 2) AS error_rate_percent
            FROM logs
        """)
        return self.cursor.fetchone()[0]

    def get_hourly_traffic(self):
        self.cursor.execute("""
            SELECT HOUR(datetime) AS hour, COUNT(*) AS requests
            FROM logs
            GROUP BY hour
            ORDER BY hour
        """)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db = MySQLHandler(host="localhost", user="root", password="root", database="log_analysis")
    print("Top Endpoints:")
    print(tabulate(db.get_top_n_endpoints(), headers=["Endpoint", "Request Count"], tablefmt="grid"))

    print("\nStatus Code Distribution:")
    print(tabulate(db.get_status_code_distribution(), headers=["Status Code", "Count"], tablefmt="grid"))

    print("\nError Rate (%):")
    print(tabulate([[db.get_error_rate()]], headers=["Error Rate (%)"], tablefmt="grid"))

    print("\nHourly Traffic:")
    print(tabulate(db.get_hourly_traffic(), headers=["Hour", "Requests"], tablefmt="grid"))

    db.close()