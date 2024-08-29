import requests
import csv
import json

# DHIS2 instance details
base_url = 'http://localhost:8080/dhis2-stable-40.4.1'
username = 'admin'
password = 'district'
program_id = 'wfd9K4dQVDR'
org_unit_id = 'GuJvMV22ihs'

# API endpoint to fetch tracked entity instances
endpoint = f'{base_url}/api/trackedEntityInstances.json?pageSize=5000&program={program_id}&ou={org_unit_id}'

# Make the API request
response = requests.get(endpoint, auth=(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
   
    # Extract tracked entity instance IDs
    tei_ids = [tei['trackedEntityInstance'] for tei in data['trackedEntityInstances']]
    
    # Print the tracked entity instance IDs
    print("Tracked Entity Instance IDs:")
    for tei_id in tei_ids:
        print(tei_id)
    
    # Write the tracked entity instance IDs to a CSV file
    with open('tracked_entity_instance_ids.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Tracked Entity Instance ID'])  # Write the header
        for tei_id in tei_ids:
            csvwriter.writerow([tei_id])
    
    print("Tracked entity instance IDs have been written to 'tracked_entity_instance_ids.csv'")
else:
    print(f"Error: Unable to fetch data (Status Code: {response.status_code})")
    print("Response content:", response.content.decode('utf-8'))  # Log the response content for debugging

