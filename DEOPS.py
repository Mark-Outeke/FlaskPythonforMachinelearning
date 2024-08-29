import requests

# DHIS2 server URL
base_url = 'https://tbl-ecbss-dev.health.go.ug'

# Your DHIS2 credentials
username = 'mak-sph.mouteke'
password = 'Mark@ecbs329'

# The program ID of the tracker program
program_id = 'wfd9K4dQVDR'

# Function to get program data elements
def get_program_data_elements(program_id):
    url = f'{base_url}/api/dataElements/?fields=id,name,shortName,aggregationType,domainType,valueType'
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    return response.json()['dataElements']

# Function to get option sets
def get_option_set(option_set_id):
    url = f'{base_url}/api/options.json/'
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    return response.json()

# Function to print options
def print_options_for_data_element(data_element):
    if 'optionSet' in data_element:
        option_set_id = data_element['optionSet']['id']
        option_set = get_option_set(option_set_id)
        options = option_set['options']
        
        print(f"Data Element: {data_element['displayName']}")
        for option in options:
            print(f"  Option ID: {option['id']}, Option Name: {option['name']}")
        print()  # Print a blank line for better readability

def main():
    print("helo")
# Retrieve program data elements
    data_elements = get_program_data_elements(program_id)

# Print options for each data element
    for data_element in data_elements:
        print_options_for_data_element(data_element)

if __name__ == "__main__":
    main()
