import pandas as pd
import json

# Function to convert JSON to CSV with specific fields
def json_to_csv(json_file_path, csv_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    # Check if json_data is a list
    if isinstance(data, list):
        for item in data:
            # Check if item is a dictionary
            if isinstance(item, dict):
                name = item.get('name', '')
                # rest of your code
            else:
                print(f"Item is not a dictionary: {item}")
    else:
        print(f"JSON data is not a list: {data}")


    # Extract the relevant fields
    extracted_data = []
    for item in data:
        name = item.get('name', '')
        optionSet_id = item.get('optionSet', {}).get('id', '')
        id = item.get('id', '')
        extracted_data.append({
            'name': name,
            'optionSet__id': optionSet_id,
            'id': id
        })
    
    # Create a DataFrame
    df = pd.DataFrame(extracted_data)
    
    # Convert to CSV
    df.to_csv(csv_file_path, index=False, sep='\t')

# Specify the paths to the JSON and CSV files
json_file_path = 'C:\\Users\\Mark Outeke\\Downloads\\optionsfordataelementmapping.json'  # Replace with the actual path to your input JSON file
csv_file_path = 'C:\\Users\\Mark Outeke\\Downloads\\optionsfordataelementmapping.csv'  # Replace with the actual path to your output CSV file

# Call the function to perform the conversion
json_to_csv(json_file_path, csv_file_path)

print(f"Successfully converted {json_file_path} to {csv_file_path}")
