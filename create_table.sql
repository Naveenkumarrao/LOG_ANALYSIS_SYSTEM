-- Table for normalized user agents
CREATE TABLE IF NOT EXISTS user_agents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_agent_string VARCHAR(512) NOT NULL UNIQUE,
    os VARCHAR(100),
    browser VARCHAR(100),
    device_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Main log entries table
CREATE TABLE IF NOT EXISTS log_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip_address VARCHAR(45) NOT NULL,
    timestamp DATETIME NOT NULL,
    method VARCHAR(10) NOT NULL,
    path VARCHAR(2048) NOT NULL,
    status_code SMALLINT NOT NULL,

    bytes_sent INT NOT NULL,
    referrer VARCHAR(2048),
    user_agent_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_agent_id) REFERENCES user_agents(id)
);

-- Indexes for performance
CREATE INDEX idx_timestamp ON log_entries (timestamp);
CREATE INDEX idx_ip_address ON log_entries (ip_address);
CREATE INDEX idx_status_code ON log_entries (status_code);
CREATE INDEX idx_path ON log_entries (path(255));