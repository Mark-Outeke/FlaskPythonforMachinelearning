import pandas as pd
import json
import random
from faker import Faker
from datetime import datetime, timedelta

# Load data
with open('C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\data_elements_info.json', 'r') as file:
    data_element_options = json.load(file)


baseline_elements = pd.read_csv("C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\BaselineElements.csv", encoding='ISO-8859-1')
enrollments = pd.read_csv("C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\enrollments.csv", encoding='ISO-8859-1')

# Define constants
program_id = 'wfd9K4dQVDR'
status_options = ['ACTIVE', 'COMPLETED']
event_status = 'COMPLETED'
tracked_entity_type = 'MCPQUTHX1Ze'
program_stage = 'o9dq0aBejXc'  # Fixed program stage
faker = Faker()

# Create a mapping of data elements to options
data_element_options_dict = {}
for element_id, details in data_element_options.items():
    data_element_options_dict[element_id] = details.get('options', [])


# Define weights for data element IDs
weights_dict = {
    'Aw9p1CCIkqL': {'Pulmonary bacteriologically confirmed (P-BC)TB': 0.57,
                 'Pulmonary Clinically Diagnosed (P-CD) TB': 0.37,
                 'Extra pulmonary (EP) TB': 0.04},
    'hDaev1EuehO': {'New': 0.933632516,
                 'Relapse': 0.042429497,
                 'Treatment after Lost to Follow up': 0.009873017,
                 'Treatment after failure': 0.003549391,
                 'Treatment history Unknown': 0.000571166,
                 'N/A': 0.009944413},
    'CxdzmL6vtnx': {'Yes': 0.94,
                     'No':0.01},
    'axDtvPeYL2Y': {'2RHZE/ 4RH': 0.99,
                    '2RHZE/ 10 RH':0.01,
                    'Specify other regimen': 0},
     'f0S6DIqAOE5': {'Yes': 0.01,
                     'No':0.99},
     'x7uZB9y0Qey': {'No AFB (0)': 0.05,
                    '1-9 AFB per 100HPF (Scanty)': 0.005,
                    '10-99 AFB per 100 HPF (+)': 0.02,
                    '1-10 AFB per HPF(++)': 0.02,
                    '> 10 AFB per HPF(+++)': 0.02,
                    'Not Done': 0.005,
                    'Contaminated': 0.00001,
                    'Others Specify':0.00001},
    'pD0tc8UxyGg':  {'MTB detected, rifampicin resistance not detected': 0.29,
                     'MTB detected, rifampicin resistance detected': 0.032,
                     'MTB detected, rifampicin resistance indeterminate':0.005 ,
                     'MTB Trace Detected RR indeterminate':0.7 ,
                     'MTB not detected': 0.001,
                     'Invalid':0.001 ,
                     'Error':0.001,
                     'No result':0.0014 },     
    'e0mTEFrXZDh' : {'Positive': 0.11,
                    'Negative': 0.82,
                    'Invalid / Indeterminate': 0.01}

}



#handle distribution of weighted elements 
def generate_weighted_value(value_type, element_id, options, incidentDate=None, orgUnitName=None):
    if value_type == 'TEXT' and element_id in weights_dict:
        weights = weights_dict[element_id]
        if all(option in weights for option in options):
            return random.choices(list(weights.keys()), weights=list(weights.values()))[0]
        else:
            # If options in JSON don't match weights, fall back to random choice
            return random.choice(options)
    elif value_type == 'TRUE_ONLY' and element_id == 't6qq4TXSE7n':
        # Distribute 20% True and 80% False
        return random.choices(['True', 'False'], weights=[0.40, 0.60])[0]
    elif value_type == 'TRUE_ONLY' and element_id == 'ig3ZDT8Mgus':
        # Distribute 20% True and 80% False
        return random.choices(['True', 'False'], weights=[0.10, 0.90])[0]
    elif value_type == 'TRUE_ONLY' and element_id == 'HHf4Vff0Xrx':
        # Distribute 20% True and 80% False
        return random.choices(['True', 'False'], weights=[0.15, 0.85])[0]
    elif value_type == 'TRUE_ONLY' and element_id == 'BQ2qwbH5WXi':
        # Distribute 20% True and 80% False
        return random.choices(['True', 'False'], weights=[0.15, 0.85])[0]
    elif value_type == 'TRUE_ONLY' and element_id == 'WqWIsCuYw14':
        # Distribute 20% True and 80% False
        return random.choices(['True', 'False'], weights=[0.175, 0.825])[0]                
    elif value_type == 'DATE' and element_id == 'EpvHxcDmxyT':
        
        return faker.date_this_decade().isoformat()
    elif value_type == 'PHONE_NUMBER':
        return faker.phone_number()
    elif value_type == 'TEXT':
        return random.choice(options) if options else faker.word()
    elif value_type == 'DATE':
        if id == 'x7uZB9y0Qey' and options:
            chosen_option = random.choices(list(weights_dict[element_id].keys()), weights=list(weights_dict[element_id].values()))[0]
            if chosen_option in ['1-9 AFB per 100HPF (Scanty)', '10-99 AFB per 100 HPF (+)', '1-10 AFB per HPF(++)', '> 10 AFB per HPF(+++)']:
                random_days = random.choice([7, 14, 21, 30])
                incident_date_dt = datetime.strptime(incident_date, "%Y-%m-%d")
                new_date = incident_date_dt + timedelta(days=random_days)
                return new_date.strftime("%Y-%m-%dT00:00:00.000")
            return faker.date_this_decade().isoformat()    
    else:
        return faker.word()



def generate_random_data_values(baseline_elements, enrollments):
    
    values = []
    enrollments = pd.read_csv("C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\enrollments.csv", encoding='ISO-8859-1')
    
    for _, row in baseline_elements.iterrows():
        element_id = row['id']
        value_type = row['valueType']
        options = data_element_options_dict.get(element_id, [])

    
        if element_id == 'f0S6DIqAOE5':
            f0S6DIqAOE5_value, random_text = generate_weighted_value(value_type, element_id, options, incident_date, org_unit_name)
            values.append({"dataElement": element_id, "value": f0S6DIqAOE5_value})
            if f0S6DIqAOE5_value == 'Yes':
                values.append({"dataElement": 'SRT2JzW4OFx', "value": random_text})
        elif element_id == 'eP1Yyb3h0ST':
            eP1Yyb3h0ST_value = generate_weighted_value(value_type, element_id, options, incident_date, org_unit_name)
            values.append({"dataElement": element_id, "value": eP1Yyb3h0ST_value})
        elif element_id == 'EpvHxcDmxyT' and f0S6DIqAOE5_value == 'Yes' and eP1Yyb3h0ST_value == 'Yes':
            new_date = (datetime.strptime(incident_date, "%Y-%m-%dT%H:%M:%S.%f") + timedelta(days=60)).isoformat()
            values.append({"dataElement": element_id, "value": new_date})
            values.append({"dataElement": 'SRT2JzW4OFx', "value": f"{new_date[:10].replace('-', '')}{org_unit_name.split()[0]}"})
        else:
            value = generate_random_value(value_type, options)
            values.append({"dataElement": element_id, "value": value})
    return values
    print(values)
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



if __name__ == "__main__":
# Prepare data by orgUnit
    org_unit_data = enrollments.groupby('orgUnit')

    # Generate JSON data
    tracked_entities = []

    # Iterate over each orgUnit and its corresponding enrollments
    for org_unit, group in org_unit_data:
        # Use trackedEntityInstance from the current group
        for _, enrollment in group.iterrows():
            instance_id = enrollment['trackedEntityInstance']
            incident_date = enrollment['enrollmentDate']  # Use enrollmentDate as incidentDate
            
            enrollments_data = [{
                "enrollment": enrollment['enrollment'],
                "program": program_id,
                "status": event_status,
                "orgUnit": org_unit,
                "incidentDate": incident_date,
                "enrollmentDate": incident_date,  # Ensure enrollmentDate matches incidentDate
                "events": [{
                    "event": "",  # Event field is left empty
                    "programStage": program_stage,
                    "orgUnit": org_unit,
                    "eventDate": incident_date,  # Event date matches incident date
                    "status": event_status,
                    "dataValues": generate_random_data_values(baseline_elements, enrollments)  # Use baseline_elements for dataValues
                }]
            }]
            
            tracked_entities.append({
                "trackedEntityInstance": instance_id,
                "trackedEntityType": tracked_entity_type,
                "orgUnit": org_unit,
                "attributes": [],
                "enrollments": enrollments_data
            })
            
            # Save to JSON file
    with open('C:\\Dev\\DevRepo\\FlaskPythonforMachinelearning\\data\\instances.json', 'w') as outfile:
        json.dump({"trackedEntityInstances": tracked_entities}, outfile, indent=4)

    print("JSON file created successfully.")
