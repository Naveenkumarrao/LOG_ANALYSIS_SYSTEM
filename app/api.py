import sys
import os

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
    traffic_by_os
)

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

@app.route('/')
def home():
    return "✅ Flask is running. Try endpoints like /top-endpoints, /top-ips, /error-rate"

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
        return jsonify(top_n_ips().to_dict())
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
        return jsonify(top_n_urls().to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/os-traffic')
def os_traffic():
    try:
        return jsonify(traffic_by_os().to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    print("🚀 Starting Flask server at http://localhost:5000")
    app.run(debug=True)


