from datetime import datetime

# Sample date string
date_string = "2023-06-26 15:30:00"

# Define the format
date_format = "%Y-%m-%d %H:%M:%S"

# Convert string to datetime
date_object = datetime.strptime(date_string, date_format)

print("Original string:", date_string)
print("Converted datetime object:", date_object)
