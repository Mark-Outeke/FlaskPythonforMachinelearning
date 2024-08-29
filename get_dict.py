import pandas as pd
import os
import codecs

# Load the CSV file

df = pd.read_csv("C:\\Users\\Mark Outeke\\Desktop\\dict.csv", encoding='ISO-8859-1')

# Display the first few rows of the DataFrame to inspect its structure
print(df.head())
def process_csv_to_json(df):
    data_elements_info = {}

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        data_element_id = row['DataElement_ID']
        option = row['OptionName']
        
        if data_element_id not in data_elements_info:
            data_elements_info[data_element_id] = {
                "options": []
            }
        
        data_elements_info[data_element_id]["options"].append(option)
    
    return data_elements_info

# Process the DataFrame to create the JSON structure
data_elements_info = process_csv_to_json(df)

# Convert to JSON string for display
import json
json_data = json.dumps(data_elements_info, indent=2)
print(json_data)
# Write the JSON data to a file
output_json_file = r'C:\Users\Mark Outeke\Desktop\data_elements_info.json'
with open(output_json_file, 'w', encoding='utf-8') as f:
    f.write(json_data)