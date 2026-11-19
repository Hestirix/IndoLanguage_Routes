
"""
Language Routes
Developed by Dennis & Neylan
Engineering in Python

Reads the first five words from forms.csv and displays
their language names using languages.csv.
"""

import csv
from pathlib import Path

# Locate the CSV files.
data_folder = Path(__file__).parent / "data"
forms_file = data_folder / "forms.csv"
languages_file = data_folder / "languages.csv"

# Store language names using their IDs.
languages = {}

with open(languages_file, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        languages[row["ID"]] = row["Name"]

# Read the words and look up their language names.
with open(forms_file, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    print("LANGUAGE ROUTES")
    print("------------------------------")
    print("First five words in our dataset:\n")

    for number, row in enumerate(reader, start=1):
        if number > 5:
            break

        word = row["Form"]
        language_id = row["Language_ID"]

        # Retrieve the language name using its ID.
        language_name = languages.get(language_id, "Unknown")

        print(f"{number}. Word: {word}")
        print(f"   Language: {language_name}")
        print(f"   Concept ID: {row['Parameter_ID']}\n")
