import csv
import random
from datetime import datetime

# File path inside repository
file_path = "data.csv"

now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H:%M:%S")

status = random.choice(["Success", "Failure"])

# Append new row
with open(file_path, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([date_str, time_str, status])

print("Updated CSV successfully.")