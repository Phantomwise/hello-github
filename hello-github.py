#!/usr/bin/env python3

import os
from datetime import datetime, timedelta

# Configuration
start_date = datetime(2026, 1, 1)  # Start date for contributions (Sunday, April 6, 2025)
pattern_file = "pattern2.txt"  # File containing the pattern

# Read the pattern from the file
with open(pattern_file, "r") as file:
    lines = file.readlines()

# Process the pattern
for row, line in enumerate(lines):
    for col, char in enumerate(line.strip()):  # Process the entire line
        if char == "#":  # Only process days with `#`
            # Calculate the commit date
            day_offset = col * 7 + row  # Calculate the day offset from the start date
            commit_date = start_date + timedelta(days=day_offset)
            commit_message = f"Hello GitHub! {commit_date.strftime('%Y-%m-%d')}, row {row}, col {col}"
            # Create an empty commit for the calculated date
            os.system(f"git commit --allow-empty --date='{commit_date.isoformat()}' -m '{commit_message}'")

# Push the commits to GitHub
# os.system("git push")