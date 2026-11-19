
"""
Language Routes
Developed by Dennis & Neylan
Engineering in Python

Reads words from forms.csv and displays their
language names and meanings using related CSV files.
"""

import csv
from pathlib import Path

# Locate the CSV files.
data_folder = Path(__file__).parent / "data"

forms_file = data_folder / "forms.csv"
languages_file = data_folder / "languages.csv"
parameters_file = data_folder / "parameters.csv"


# Load language names into a dictionary.
languages = {}

with open(languages_file, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        languages[row["ID"]] = row["Name"]


# Load concept names into another dictionary.
concepts = {}

with open(parameters_file, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        concepts[row["ID"]] = row["Name"]


# Read the first five words.
with open(forms_file, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    print("LANGUAGE ROUTES")
    print("------------------------------")
    print("First five words in our dataset:\n")

    for number, row in enumerate(reader, start=1):
        if number > 10:
            break

        word = row["Form"]
        language_id = row["Language_ID"]
        concept_id = row["Parameter_ID"]

        # Retrieve matching names from the dictionaries.
        language_name = languages.get(language_id, "Unknown")
        meaning = concepts.get(concept_id, "Unknown")

        print(f"{number}. Word: {word}")
        print(f"   Language: {language_name}")
        print(f"   Meaning: {meaning}\n")
