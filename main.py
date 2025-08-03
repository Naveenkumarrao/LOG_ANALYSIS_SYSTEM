import sys
import os
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from flask import Flask, jsonify, render_template
from app.analysis import (
    most_common_endpoints,
    error_rate,
    status_code_distribution,
    top_n_ips,
    hourly_distribution,
    daily_distribution,
    top_n_urls,
    traffic_by_os,
    error_logs
)

from tabulate import tabulate

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

# ------------------- CLI FUNCTIONS ------------------- #
def generate_report(report_type, *args):
    try:
        if report_type == "top_n_ips":
            n = int(args[0]) if args else 10
            result = top_n_ips(n)
        elif report_type == "status_code_distribution":
            result = status_code_distribution()
        elif report_type == "hourly_traffic":
            result = hourly_distribution()
        elif report_type == "daily_traffic":
            result = daily_distribution()
        elif report_type == "top_n_urls":
            n = int(args[0]) if args else 10
            result = top_n_urls(n)
        elif report_type == "os_distribution":
            result = traffic_by_os()
        elif report_type == "error_logs":
            code = int(args[0]) if args else 404
            result = error_logs(code)
        else:
            print("❌ Invalid report type.")
            return

        if isinstance(result, pd.DataFrame):
            print(tabulate(result, headers='keys', tablefmt='psql'))
        elif isinstance(result, pd.Series):
            print(tabulate(result.reset_index(), headers=["Value", "Count"], tablefmt='psql'))
        else:
            print(result)

    except Exception as e:
        print(f"❌ Error generating report: {e}")

# ------------------- FLASK ROUTES ------------------- #
@app.route('/')
def home():
    return "✅ Flask is running. Visit routes like /top-endpoints, /top-ips, /error-rate etc."

@app.route('/top-endpoints')
def top_endpoints():
    try:
        return jsonify(most_common_endpoints().to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/error-rate')
def error_rate_api():
    try:
        return jsonify({"error_rate": error_rate()})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/status-codes')
def status_codes():
    try:
        return jsonify(status_code_distribution().to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/top-ips')
def top_ips():
    try:
        return jsonify(top_n_ips(10).to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/hourly-distribution')
def hourly_dist():
    try:
        return jsonify(hourly_distribution().to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/daily-distribution')
def daily_dist():
    try:
        return jsonify(daily_distribution().to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/top-urls')
def top_urls():
    try:
        return jsonify(top_n_urls(10).to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/os-traffic')
def os_traffic():
    try:
        return jsonify(traffic_by_os().to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/error-logs/<int:code>')
def error_logs_api(code):
    try:
        return jsonify(error_logs(code).to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

# ------------------- ENTRY POINT ------------------- #
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "generate_report":
        generate_report(*sys.argv[2:])
    else:
        print("🚀 Starting Flask server at http://localhost:5000")
        app.run(debug=True)
