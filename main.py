
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



# Ask the user which word they want to find.
print("LANGUAGE ROUTES")
print("------------------------------")

search_word = input("Enter a word to search: ").strip().casefold()

# Keep track of how many matching words we find.
matches = 0

# Open the dataset and search through its records.
with open(forms_file, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        word = row["Form"]

        # Compare the dataset word with the user's input.
        if search_word and word.strip().casefold() == search_word:
            matches += 1

            language_id = row["Language_ID"]
            concept_id = row["Parameter_ID"]

            language_name = languages.get(language_id, "Unknown")
            meaning = concepts.get(concept_id, "Unknown")

            print(f"\nResult {matches}")
            print(f"Word: {word}")
            print(f"Language: {language_name}")
            print(f"Meaning: {meaning}")

# Display a message if the search found nothing.
if matches == 0:
    print("\nNo matching word was found.")

print(f"\nTotal matches: {matches}")



# Display the first 10 German words in the dataset.
print("\nFIRST 10 GERMAN WORDS")
print("------------------------------")

count = 0

with open(forms_file, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Language_ID"] == "27":
            count += 1

            print(f"{count}. {row['Form']}")

            if count == 10:
                break
