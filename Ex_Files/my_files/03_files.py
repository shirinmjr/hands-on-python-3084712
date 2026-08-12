import csv
import json
from pprint import pprint
from datetime import datetime

# Reading the CSV file
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)
# Printing the laureate with the surname "Einstein" from the list of laureates
for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        print("____________")
        year_date = datetime.strptime(laureate["year"], "%Y") # Parse the year field into a datetime object
        born_date = datetime.strptime(laureate["born"], "%Y-%m-%d") # Parse the born field into a datetime object
        print("age", year_date.year - born_date.year) # Calculate the age by subtracting
        break

    with open("laureates.json", "w") as f:
        json.dump(laureates,f, indent=2) # Write the list of laureates to a JSON file with indentation for readability
print("____________")
###########################################
# Seting the CSV string and the dictionary for Albert Einstein
EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'
# this is a dictionary representation of the CSV string for Albert Einstein
# the dictionary keys are the column names and the values are the corresponding values from the CSV string
# the difference between the CSV string and the dictionary is
# that the CSV string is a single line of text,
#  while the dictionary is a structured data type that allows for easy access to the values using the keys
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}
# This converts the dictionary to a JSON string
einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json) # This converts the JSON string back to a dictionary
print( einstein_json) # This prints the JSON string representation of the EINSTEIN dictionary
print("-----------=>OBJECT")
pprint( back_to_dict) # This pretty prints the dictionary

##########Challenge: Write a function that takes a list of laureates and returns a list of laureates who name starts with the letter "A"
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

laureates_beginning_with_a = []
for laureate in laureates:
    if laureate ["name"][0] == "A":
        laureates_beginning_with_a.append(laureate)

print ("laureates_beginning_with_a", laureates_beginning_with_a)

with open ("laureates_starting_with_a.json", "w") as f:
    json.dump(laureates_beginning_with_a, f, indent=2) # Write the list of laureates whose names start with "A" to a JSON file with indentation for readability

# NOTE:
# Difference beween json.dump and json.dumps is that json.dump writes the JSON data to a file,
# while json.dumps returns the JSON data as a string.
# json.dumps is similar to the built-in str() function in javascript,
#  which converts a JavaScript object to a string representation.