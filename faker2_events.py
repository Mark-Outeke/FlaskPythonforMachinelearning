import pandas as pd
import json
import random
from faker import Faker

# Load data
with open('C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\data_elements_info.json', 'r') as file:
    data_element_options = json.load(file)

# Load the BaselineElements.csv file
baseline_elements = pd.read_csv("C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\BaselineElements.csv", encoding='ISO-8859-1')

# Define constants
faker = Faker()

# Create a mapping of data elements to options
data_element_options_dict = {}
for element_id, details in data_element_options.items():
    data_element_options_dict[element_id] = details.get('options', [])

def generate_random_value(value_type, options):
    if value_type == 'TEXT':
        return random.choice(options) if options else faker.word()
    elif value_type == 'DATE':
        return faker.date_this_decade().isoformat()
    elif value_type == 'PHONE_NUMBER':
        return faker.phone_number()
    elif value_type == 'NUMERIC':
        return faker.random_number(digits=3, fix_len=True)  # Adjust digits as needed
    else:
        return faker.word()

def generate_random_data_values(baseline_elements):
    values = []
    for _, row in baseline_elements.iterrows():
        element_id = row['id']
        value_type = row['valueType']
        options = data_element_options_dict.get(element_id, [])
        
        value = generate_random_value(value_type, options)
        values.append({
            "dataElement": element_id,
            "value": value
        })
    return values

# Generate random data values
data_values = generate_random_data_values(baseline_elements)

# Print the generated data values (for demonstration)
print(json.dumps(data_values, indent=4))

# Optionally save to a JSON file
with open('C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\generated_data_values.json', 'w') as outfile:
    json.dump(data_values, outfile, indent=4)

print("Random data values generated and saved successfully.")
