import pandas as pd
import mysql.connector
import re

def fetch_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="log_analysis"
    )
    df = pd.read_sql("SELECT * FROM logs", conn)
    conn.close()
    return df

def most_common_endpoints(n=5):
    df = fetch_data()
    return df['endpoint'].value_counts().head(n)

def status_code_distribution():
    df = fetch_data()
    return df['status_code'].value_counts()

def error_rate():
    df = fetch_data()
    total = len(df)
    errors = len(df[df['status_code'] >= 400])
    return round(errors / total * 100, 2)

def top_n_ips(n=10):
    df = fetch_data()
    return df['ip'].value_counts().head(n)

def hourly_distribution():
    df = fetch_data()
    df['hour'] = pd.to_datetime(df['datetime']).dt.hour
    return df['hour'].value_counts().sort_index()

def daily_distribution():
    df = fetch_data()
    df['day'] = pd.to_datetime(df['datetime']).dt.day_name()
    return df['day'].value_counts().reindex([
        'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    ])

def top_n_urls(n=10):
    df = fetch_data()
    return df['endpoint'].value_counts().head(n)

def error_logs(status_code):
    conn = connect_db()
    df = pd.read_sql("SELECT * FROM logs", conn)
    conn.close()

    return df[df['status_code'] == status_code][['ip', 'datetime', 'endpoint', 'status_code']]


def traffic_by_os():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="log_analysis"
    )
    ua_df = pd.read_sql("""
        SELECT ua.user_agent FROM user_agents ua
        JOIN logs l ON ua.log_entry_id = l.id
    """, conn)
    conn.close()

    def extract_os(ua):
        ua = ua.lower() if ua else ''
        if 'windows' in ua:
            return 'Windows'
        elif 'linux' in ua:
            return 'Linux'
        elif 'mac' in ua:
            return 'MacOS'
        elif 'android' in ua:
            return 'Android'
        elif 'iphone' in ua or 'ios' in ua:
            return 'iOS'
        else:
            return 'Other'

    ua_df['os'] = ua_df['user_agent'].apply(extract_os)
    return ua_df['os'].value_counts()

def error_logs(code):
    df = fetch_data()
    return df[df['status_code'] == code][['ip', 'datetime', 'endpoint', 'status_code']]
