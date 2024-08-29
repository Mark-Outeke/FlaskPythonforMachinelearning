import requests
import csv
import json

# DHIS2 instance details
base_url = 'http://localhost:8080/dhis2-stable-40.4.1'
username = 'admin'
password = 'district'
program_id = 'your_program_id'  # Replace with your program ID

# Helper function to make authenticated GET requests
def get_request(endpoint):
    response = requests.get(endpoint, auth=(username, password))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data from {endpoint} (Status Code: {response.status_code})")
        print("Response content:", response.content.decode('utf-8'))
        return None

# Fetch program stages for the given program
program_stages_endpoint = f'{base_url}/api/programStages?filter=program.id:eq:{program_id}&fields=id,name&paging=false'
program_stages_data = get_request(program_stages_endpoint)

if program_stages_data:
    program_stages = program_stages_data['programStages']
    
    # Collect data elements information
    data_elements_info = []
    
    for stage in program_stages:
        stage_id = stage['id']
        stage_name = stage['name']
        print(f"Fetching data elements for program stage: {stage_name} (ID: {stage_id})")
        
        # Fetch data elements for the program stage
        data_elements_endpoint = f'{base_url}/api/programStages/{stage_id}?fields=programStageDataElements[dataElement[id,name,optionSet[id,name,options[id,name]]]]'
        stage_data = get_request(data_elements_endpoint)
        
        if stage_data:
            program_stage_data_elements = stage_data['programStageDataElements']
            
            for psde in program_stage_data_elements:
                data_element = psde['dataElement']
                data_element_id = data_element['id']
                data_element_name = data_element['name']
                
                if 'optionSet' in data_element:
                    option_set = data_element['optionSet']
                    option_set_id = option_set['id']
                    option_set_name = option_set['name']
                    options = option_set['options']
                    option_names = [option['name'] for option in options]
                else:
                    option_set_id = None
                    option_set_name = None
                    option_names = []
                
                data_elements_info.append([
                    stage_id, stage_name, 
                    data_element_id, data_element_name, 
                    option_set_id, option_set_name, 
                    ", ".join(option_names)
                ])
    
    # Write the data elements info to a CSV file
    with open('data_elements_info.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([
            'Program Stage ID', 'Program Stage Name', 
            'Data Element ID', 'Data Element Name', 
            'Option Set ID', 'Option Set Name', 'Options'
        ])  # Write the header
        for info in data_elements_info:
            csvwriter.writerow(info)
    
    print("Data elements information has been written to 'data_elements_info.csv'")
