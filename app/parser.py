import re
from datetime import datetime

log_pattern = r'(\S+) - - \[(.*?)\] "(.*?)" (\d{3}) (\d+)'

def parse_log_line(line):
    match = re.match(log_pattern, line)
    if match:
        ip = match.group(1)
        dt_str = match.group(2)
        dt = datetime.strptime(dt_str, "%d/%b/%Y:%H:%M:%S %z")
        request = match.group(3).split()
        if len(request) == 3:
            method, endpoint, protocol = request
        else:
            method = endpoint = protocol = "-"
        status = int(match.group(4))
        size = int(match.group(5))
        return (ip, dt, method, endpoint, protocol, status, size)
    return None
