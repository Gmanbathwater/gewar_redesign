import csv
import json

def csv_to_json(csv_file, json_file):
    # Read the CSV file with UTF-8 encoding
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Convert each row into a dictionary
        data = [row for row in reader]

    # Write the JSON data to a file with UTF-8 encoding
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

# Specify the input CSV file and output JSON file
csv_file = '/path/to/input.csv'
json_file = '/path/to/output.json'

# Call the function to convert CSV to JSON
csv_to_json("C:/Users/levi/Documents/vscode code/City decoder/worldcities.csv", "C:/Users/levi/Documents/vscode code/City decoder/file.json")