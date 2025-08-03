import mysql.connector

def insert_log(record):
    conn = mysql.connector.connect(
        host="localhost", user="root", password="root", database="log_analysis"
    )
    cursor = conn.cursor()
    sql = """INSERT INTO logs (ip, datetime, method, endpoint, protocol, status_code, size)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, record)
    conn.commit()
    cursor.close()
    conn.close()
