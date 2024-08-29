import requests
import csv

# Define DHIS2 API endpoint and credentials
api_url = 'https://tbl-ecbss-dev.health.go.ug/api/40/trackedEntityInstances'
username = 'mak-sph.mouteke'
password = 'Mark@ecbs329'

# Make API request to retrieve tracked entity instances
response = requests.get(api_url, auth=(username, password))

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    
    # Open CSV file for writing
    with open('tracker_data.csv', 'w', newline='') as csvfile:
        # Define CSV writer
        csv_writer = csv.writer(csvfile)
        
        # Write header row
        csv_writer.writerow(['Tracked Entity ID', 'Attribute 1', 'Attribute 2', ...])
        
        # Iterate over tracked entity instances and write data to CSV
        for instance in data['trackedEntityInstances']:
            tracked_entity_id = instance['trackedEntityInstance']
            attributes = instance['attributes']
            # Extract attribute values based on attribute IDs
            attribute_values = [attr['value'] for attr in attributes]
            # Write row to CSV
            csv_writer.writerow([tracked_entity_id] + attribute_values)
            
    print("CSV file created successfully.")
else:
    print("Failed to retrieve data from DHIS2.")
