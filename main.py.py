
"""
Language Routes
Developed by Dennis & Neylan
Engineering in Python

This program reads a linguistic dataset and displays
the first five words and their identifiers.
"""

import csv
from pathlib import Path

# Locate the dataset relative to this Python file.
file_path = Path(__file__).parent / "data" / "forms.csv"

# Open the CSV file and read its contents.
with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    print("LANGUAGE ROUTES")
    print("------------------------------")
    print("First five words in our dataset:\n")

    # Read and display only the first five records.
    for number, row in enumerate(reader, start=1):
        if number > 5:
            break

        print(f"{number}. Word: {row['Form']}")
        print(f"   Language ID: {row['Language_ID']}")
        print(f"   Concept ID: {row['Parameter_ID']}\n")
