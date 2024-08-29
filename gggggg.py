import requests

# DHIS2 server URL
base_url = 'https://tbl-ecbss-dev.health.go.ug'

# Your DHIS2 credentials
username = 'mak-sph.mouteke'
password = 'Mark@ecbs329'

# The program ID of the tracker program
program_id = 'wfd9K4dQVDR'

# Function to get tracked entity attributes for a program
def get_tracked_entity_attributes(program_id):
    url = f'{base_url}/api/programs/{program_id}/trackedEntityAttributes'
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    return response.json()['trackedEntityAttributes']

# Function to get options for an option set
def get_option_set(option_set_id):
    url = f'{base_url}/api/optionSets/{option_set_id}'
    response = requests.get(url, auth=(username, password))
    response.raise_for_status()
    return response.json()

# Retrieve tracked entity attributes
tracked_entity_attributes = get_tracked_entity_attributes(program_id)

# Retrieve options for each option set
options = {}
for attribute in tracked_entity_attributes:
    if 'optionSet' in attribute:
        option_set_id = attribute['optionSet']['id']
        option_set = get_option_set(option_set_id)
        options[option_set_id] = option_set['options']

# Print options
for option_set_id, option_list in options.items():
    print(f'Options for Option Set ID {option_set_id}:')
    for option in option_list:
        print(f"- {option['name']}")

