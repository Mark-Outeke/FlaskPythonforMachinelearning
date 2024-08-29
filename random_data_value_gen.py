import json
import pandas as pd
import random
import encodings


# Step 1: Load Data Elements JSON and Baseline Elements CSV, enrollments and OrgUnits
with open('C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\data_elements_info.json', 'r') as file:
    data_elements = json.load(file)


baseline_elements = pd.read_csv("C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\BaselineElements.csv", encoding='ISO-8859-1')
program_stages = 'o9dq0aBejXc'

orgUnits = ['yApOnywci25','Q6qNTXu3yRx','GuJvMV22ihs']

enrollments = pd.read_csv("C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\enrollments.csv", encoding='ISO-8859-1')

# Step 2: Extract Data Element IDs and Options
data_elements_dict = {}
for element in data_elements['dataElements']:
    element_id = element['id']
    options = [option['name'] for option in element['optionSet']['options']] if 'optionSet' in element and element['optionSet'] else []
    data_elements_dict[element_id] = options

# Step 3: Generate Random Data Values
def generate_random_values(data_elements_dict, num_records=10):
    records = []
    for _ in range(num_records):
        record = {}
        for element_id, options in data_elements_dict.items():
            record[element_id] = random.choice(options) if options else None
        records.append(record)
    return records

num_records = 10  # Number of random records to generate
random_data_values = generate_random_values(data_elements_dict, num_records)

# Step 4: Create JSON Structure
output_json = {
    "dataValues": random_data_values
}

# Step 5: Save to a JSON file
with open('/mnt/data/random_data_values.json', 'w') as file:
    json.dump(output_json, file, indent=4)
