import json

import requests


# Set your DHIS2 credentials and base URL

base_url = 'https://tbl-ecbss-dev.health.go.ug'

username = 'mak-sph.mouteke'

password = 'Mark@ecbs329'

program_id = 'wfd9K4dQVDR'


# Function to get program data elements

def get_program_data_elements(program_id):

    url = f'{base_url}/api/dataElements/?paging=false&fields=id,name,shortName,aggregationType,domainType,valueType,optionSet'

    response = requests.get(url, auth=(username, password))

    response.raise_for_status()

    return response.json()['dataElements']


# Function to get option sets

def dhisApi_get_option_set():

    url = f'{base_url}/api/optionSets.json?paging=false&fields=id,name,options'

    response = requests.get(url, auth=(username, password))

    response.raise_for_status()

    return response.json()


# Function to print options

def print_options_for_data_element(data_element):
    if 'optionSet' in data_element:
        apiOptions = dhisApi_get_option_names_for_option_ids();
        option_set_id = data_element['optionSet']['id']
        results = dhisApi_get_option_set();

        optionSets = results['optionSets']
        #print(f"{data_element['name']}")
        for optionSet in optionSets:
            
            if(option_set_id == optionSet['id']):
                #optionSet['options'] = 
                #data_element['optionSet'] = optionSet
                print(optionSet)
                break




                optionSetOptions = optionSet['options']
                for optionSetOption in optionSetOptions:
                    for apiOption in apiOptions:
                        if apiOption['id'] == optionSetOption['id']:
                            #print(f"OptionSet<ID: {optionSet['id']} Name:{optionSet['name']}>  Option ID: {optionSetOption['id']} Option Name: {apiOption['name']}")
                            listOfOptions.append(apiOption)
                
                break
            
            
            #print(data_element)
        print()  # Print a blank line for better readability

#function to retrieve option names

def dhisApi_get_option_names_for_option_ids():
    url = f'{base_url}/api/options.json?paging=false&fields=id,name,optionSet'

    response = requests.get(url, auth=(username, password))

    response.raise_for_status()
    
    return response.json()['options']
    
# Function to save data elements and options to a JSON file

def save_to_json(data_elements, filename):

    data_elements_with_options = []
    

    for data_element in data_elements:

        if 'optionSet' in data_element:

            option_set_id = data_element['optionSet']['id']

            option_set = dhisApi_get_option_set(option_set_id)

            data_element['options'] = option_set['options']

        data_elements_with_options.append(data_element)
    

    with open(filename, 'w') as json_file:

        json.dump(data_elements_with_options, json_file, indent=4)


def main():

    print("Starting to retrieve data elements and options...")

    # Retrieve program data elements

    data_elements = get_program_data_elements(program_id)


    # Print options for each data element

    for data_element in data_elements:
        print_options_for_data_element(data_element)
    

    # Save data elements and options to a JSON file

    #save_to_json(data_elements, 'data_elements_with_options.json')

    print("Data elements and options saved to data_elements_with_options.json")


if __name__ == "__main__":
    main()

