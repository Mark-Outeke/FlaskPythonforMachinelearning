import json
import requests
import csv
import os

# Set your DHIS2 credentials and base URL
base_url = 'https://tbl-ecbss-dev.health.go.ug'

username = 'mak-sph.mouteke'

password = 'Mark@ecbs329'

program_id = 'wfd9K4dQVDR'

# Function to get program data elements
def get_program_data_elements(program_id):
    url = f'{base_url}/api/dataElements.json?paging=false&fields=id,name,shortName,aggregationType,domainType,valueType,optionSet[id]'
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    return response.json()['dataElements']

# Function to get option sets
def dhisApi_get_option_set():
    url = f'{base_url}/api/optionSets.json?paging=false&fields=id,name,options'
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    return response.json()

# Function to get option names for option IDs
def dhisApi_get_option_names_for_option_ids():
    url = f'{base_url}/api/options.json?paging=false&fields=id,name'
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    return response.json()['options']

# Function to print options for each data element
def print_options_for_data_element(data_element, apiOptions, optionSets):
    if 'optionSet' in data_element:
        option_set_id = data_element['optionSet']['id']
        
        for optionSet in optionSets:
            if option_set_id == optionSet['id']:
                print(f"Data Element: {data_element['name']}")
                
                optionSetOptions = optionSet['options']
                listOfOptions = []
                for optionSetOption in optionSetOptions:
                    for apiOption in apiOptions:
                        if apiOption['id'] == optionSetOption['id']:
                            listOfOptions.append(apiOption)
                            print(f"  Option ID: {apiOption['id']}, Option Name: {apiOption['name']}")
                print()  # Print a blank line for better readability
                break

# Function to save data elements and options to a JSON file
def save_to_json(data_elements, apiOptions, optionSets, filename):
    data_elements_with_options = []
    
    for data_element in data_elements:
        if 'optionSet' in data_element:
            option_set_id = data_element['optionSet']['id']
            
            for optionSet in optionSets:
                if option_set_id == optionSet['id']:
                    optionSetOptions = optionSet['options']
                    listOfOptions = []
                    for optionSetOption in optionSetOptions:
                        for apiOption in apiOptions:
                            if apiOption['id'] == optionSetOption['id']:
                                listOfOptions.append(apiOption)
                    data_element['options'] = listOfOptions
                    break
        
        data_elements_with_options.append(data_element)
    
    with open(filename, 'w') as json_file:
        json.dump(data_elements_with_options, json_file, indent=4)
def save_to_csv(data_elements, apiOptions, optionSets, filename):
    header = ['Data Element ID', 'Data Element Name', 'Option Set ID', 'Option ID', 'Option Name']
    rows = []
    
    for data_element in data_elements:
        if 'optionSet' in data_element:
            option_set_id = data_element['optionSet']['id']
            
            for optionSet in optionSets:
                if option_set_id == optionSet['id']:
                    optionSetOptions = optionSet['options']
                    for optionSetOption in optionSetOptions:
                        for apiOption in apiOptions:
                            if apiOption['id'] == optionSetOption['id']:
                                rows.append([
                                    data_element['id'],
                                    data_element['name'],
                                    option_set_id,
                                    apiOption['id'],
                                    apiOption['name']
                                ])
                    break
    
    with open(filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(rows)
def main():
    print("Starting to retrieve data elements and options...")

    # Retrieve program data elements
    data_elements = get_program_data_elements(program_id)
    
    # Retrieve option names and option sets
    apiOptions = dhisApi_get_option_names_for_option_ids()
    optionSets = dhisApi_get_option_set()['optionSets']

    # Print options for each data element
    for data_element in data_elements:
        print_options_for_data_element(data_element, apiOptions, optionSets)
    
    # Save data elements and options to a JSON file
    save_to_json(data_elements, apiOptions, optionSets, 'data_elements_with_options.json')
    print("Data elements and options saved to data_elements_with_options.json")
    # Save data elements and options to a CSV file
    save_to_csv(data_elements, apiOptions, optionSets, 'data_elements_with_options.csv')
    print("Data elements and options saved to data_elements_with_options.csv")
if __name__ == "__main__":
    main()
