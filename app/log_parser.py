import pandas as pd
import re

# Step 1: Parse the raw log file into structured data
log_file = "access_log.log"

# You can adjust this regex based on your log format
pattern = r'(?P<ip>\S+) \S+ \S+ \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<endpoint>\S+) (?P<protocol>\S+)" (?P<status_code>\d{3}) (?P<size>\S+) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"'

data = []
with open(log_file, "r") as file:
    for line in file:
        match = re.match(pattern, line)
        if match:
            data.append(match.groupdict())

# Step 2: Load into DataFrame
df = pd.DataFrame(data)

# Step 3: Check for null/missing values
null_counts = df.isnull().sum()
print("🔍 Missing (null) values in each column:")
print(null_counts)

# Step 4: Check for suspicious values like '-' or empty string
print("\n⚠️ Suspicious values like '-' or empty strings:")
for col in df.columns:
    dash_count = (df[col] == '-').sum()
    empty_count = (df[col] == '').sum()
    print(f"{col}: {dash_count} dashes, {empty_count} empty strings")

# (Optional) Step 5: Save the report
with open("log_data_quality_report.txt", "w") as f:
    f.write("Missing (null) values:\n")
    f.write(str(null_counts) + "\n\n")
    f.write("Suspicious '-' or '' values:\n")
    for col in df.columns:
        dash_count = (df[col] == '-').sum()
        empty_count = (df[col] == '').sum()
        f.write(f"{col}: {dash_count} dashes, {empty_count} empty strings\n")
# Clean data (remove rows with '-' or empty values)
df_cleaned = df.copy()
for col in df_cleaned.columns:
    df_cleaned = df_cleaned[~(df_cleaned[col].isin(['-', '']))]

# Save cleaned data
df_cleaned.to_csv("cleaned_logs.csv", index=False)
print(f"\n✅ Cleaned logs saved to cleaned_logs.csv")
