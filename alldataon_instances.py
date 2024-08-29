import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

# DHIS2 server URL
base_url = 'https://tbl-ecbss-dev.health.go.ug'

# Your DHIS2 credentials
username = 'mak-sph.mouteke'
password = 'Mark@ecbs329'

# Function to get data elements mapping (id -> name)
def get_data_elements():
    url = f"{base_url}/api/dataElements.json?paging=false&fields=id,name"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    response.raise_for_status()
    data = response.json()
    return {element['id']: element['name'] for element in data['dataElements']}

# Function to get all tracked entity instances with their events and data values
def get_tracked_entity_instances():
    url = f"{base_url}/api/trackedEntityInstances.json?fields*&trackedEntityType=aP2ziFSDvV4&ou=GuJvMV22ihs"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    response.raise_for_status()
    return response.json()['trackedEntityInstances']

# Get data elements mapping
data_elements = get_data_elements()

# Get tracked entity instances
tei_data = get_tracked_entity_instances()

# Prepare data for DataFrame
rows = []
for tei in tei_data:
    for enrollment in tei.get('enrollments', []):
        for event in enrollment.get('events', []):
            row = {
                'trackedEntityInstance': tei['trackedEntityInstance'],
                'orgUnit': tei['orgUnit'],
                'event': event['event']
            }
            for data_value in event.get('dataValues', []):
                data_element_id = data_value['dataElement']
                data_element_name = data_elements.get(data_element_id, data_element_id)
                row[data_element_name] = data_value['value']
            rows.append(row)

# Create DataFrame
df = pd.DataFrame(rows)

# Save DataFrame to CSV (optional)
df.to_csv('tracked_entity_instances.csv', index=False)

print("Data extraction completed successfully.")
