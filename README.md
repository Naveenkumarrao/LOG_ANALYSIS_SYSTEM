# 🔍 Log File Analysis & Reporting System

A Python Flask-based log analyzer that processes Apache-style access logs, stores them in a MySQL database, and provides interactive reports via a Chart.js dashboard.

---

## 📁 Project Structure

log-analysis-system/
│
├── app/
│ ├── init.py # Package initializer
│ ├── analysis.py # Business logic for data analysis
│ ├── api.py # Flask app with API endpoints
│ ├── db.py # MySQL database connection
│ ├── log_parser.py # Log parsing logic
│ ├── mysql_handler.py # Log insertion into MySQL
│ ├── parser.py # Regex-based parsing
│ └── templates/
│ └── dashboard.html # HTML dashboard UI
│
├── data/
│ ├── access_log.log # Sample Apache log file
│
├── create_table.sql # SQL script to create logs table
├── load_to_mysql.py # CLI tool to load logs into MySQL
├── main.py # CLI entry point
├── requirements.txt # Python package dependencies
└── README.md # Project documentation

## 🚀 Features

- Flask REST API for log analytics
- Parses Apache log format
- MySQL integration for persistent storage
- CLI script to ingest logs


- Endpoints:
  - Status Code Distribution
  - Hourly & Daily Requests
  - Top IPs, URLs
  - Error Rate and more

  ## 🐍 Usage Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt

#Set up MySQL Table
mysql -u root -p < create_table.sql


 #Load Log File into MySQL
python load_to_mysql.py data/access_log.log

#Start the Flask App
python app/api.py

#Then open your browser and navigate to:
http://127.0.0.1:5000/dashboard

⚙ Configuration
Edit db.py to configure your MySQL credentials
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your-password",
    database="log_analysis"
)


 Requirements
Python 3.8+
sql
flask
mysql-connector-python

👨‍💻 Author
Naveen Kumar Chennamaneni
📧 naveenkumarchennamaneni@gmail.com

