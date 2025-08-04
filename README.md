# 🔍 Log File Analysis & Reporting System

A command-line and web-based system that parses Apache-style access logs, stores them in a MySQL database, and provides insightful analytics through a PHP + Chart.js dashboard.

---

## 📁 Project Structure

```
Project-1-log-analysis-and-report/
│
├── dashboard/                  # PHP Web Dashboard
│   ├── index.php               # Main dashboard UI
│   ├── reports.php             # API for chart/report data
│   ├── db.php                  # MySQL connection handler
│   ├── style.css               # Styling for dashboard
│   └── main.js                 # Chart logic and fetch requests
│
├── log_analyzer_cli/           # Python CLI Tool
│   ├── main.py                 # CLI entry point
│   ├── log_parser.py           # Parses Apache logs using regex
│   ├── mysql_handler.py        # Handles MySQL inserts and queries
│   ├── config.ini              # DB credentials and regex config
│   ├── generate_realistic_logs.py # Generates sample logs for testing
│   ├── requirements.txt        # Python dependencies
│   ├── sample_logs/            # Folder containing sample logs
│   └── sql/                    # SQL scripts to create DB tables
```

---

## 🚀 Features

- ✅ Command-line interface for log processing
- ✅ Apache log parsing using regex
- ✅ Device/OS/User-Agent extraction
- ✅ MySQL database storage
- ✅ PHP + Chart.js dashboard with:
  - Status Code Distribution
  - Hourly Traffic Report
  - OS/Device Distribution
  - Top IP Addresses
  - Top Requested URLs

---

## 🐍 CLI Usage (Python)

```bash
# Process a log file
python main.py process_logs sample_logs/access.log

# Generate specific reports
python main.py generate_report status_code_distribution
python main.py generate_report hourly_traffic
python main.py generate_report os_distribution
python main.py generate_report top_n_ips 5
python main.py generate_report top_n_urls 5
```

---

## 🌐 Web Dashboard (PHP)

Start the built-in PHP server:

```bash
cd dashboard
php -S localhost:8000
```

Then open in your browser: [http://localhost:8000](http://localhost:8000)

---

## ⚙ Configuration

Edit `config.ini` to update MySQL and regex details:

```ini
[mysql]
host = localhost
port = 3306
user = root
password = your_password
database = project1

[log]
regex = ^(?P<ip>[\d\.]+) - - \[(?P<datetime>[^\]]+)\] "(?P<request>[^"]+)" (?P<status>\d{3}) (?P<size>\d+|-) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]+)"
```

---

## 📦 Dependencies

### Python
- `mysql-connector-python`
- `tabulate`
- `argparse`, `logging`, `re` (built-in)

Install using:

```bash
pip install -r requirements.txt
```

### PHP
- PHP 8+
- MySQLi or PDO extension enabled

---

## 🛠 SQL Schema

Run the following SQL script (found in `sql/create_table.sql`) to create the required table:

```sql
CREATE TABLE logs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  ip VARCHAR(45),
  datetime DATETIME,
  method VARCHAR(10),
  url TEXT,
  protocol VARCHAR(10),
  status_code INT,
  response_size INT,
  user_agent TEXT,
  os VARCHAR(50),
  device VARCHAR(50)
);
```

---

## 📧 Author

Developed by **Naveen Kumar Rao**  
📫 Contact: [your-email@example.com] *(Replace with your actual email or GitHub)*

---

## 📝 License

This project is open-source and free to use for learning and development purposes.