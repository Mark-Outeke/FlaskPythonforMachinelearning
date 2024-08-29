import json
import uuid
from datetime import datetime
import string
import random

# Sample input JSON file with tracked entity instances
input_file = 'tracked_entity_instances.json'

# Output JSON file
output_file = 'generated_events.json'

# Sample data for the program stages and data elements
program_stages = [
    {"stage": "1", "name": "Baseline Information"},
    {"stage": "2", "name": "Lab Tests / Other Investigations"},
    {"stage": "3", "name": "DOT"},
    {"stage": "4", "name": "Contact Screening & Management"},
    {"stage": "5", "name": "Community Followup"},
    {"stage": "6", "name": "Post-TB treatment monitoring"},
    {"stage": "7", "name": "Treatment Outcome"},
    {"stage": "8", "name": "Treatment"}
]

data_elements = {
    "1": ["DATA_ELEMENT_ID_BASELINE_1", "DATA_ELEMENT_ID_BASELINE_2"],
    "2": ["DATA_ELEMENT_ID_LAB_1", "DATA_ELEMENT_ID_LAB_2"],
    "3": ["DATA_ELEMENT_ID_DOT_1", "DATA_ELEMENT_ID_DOT_2"],
    "4": ["DATA_ELEMENT_ID_CONTACT_1", "DATA_ELEMENT_ID_CONTACT_2"],
    "5": ["DATA_ELEMENT_ID_COMMUNITY_1", "DATA_ELEMENT_ID_COMMUNITY_2"],
    "6": ["DATA_ELEMENT_ID_POST_TB_1", "DATA_ELEMENT_ID_POST_TB_2"],
    "7": ["DATA_ELEMENT_ID_TREATMENT_OUTCOME_1", "DATA_ELEMENT_ID_TREATMENT_OUTCOME_2"],
    "8": ["DATA_ELEMENT_ID_TREATMENT_1", "DATA_ELEMENT_ID_TREATMENT_2"]
}

program_id = "DSTB_PROGRAM_ID"
org_unit_id = "ORG_UNIT_ID"

# Helper function to generate a unique ID
def generate_unique_event_id(length=11):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))
event_id = generate_unique_event_id()
# Helper function to generate event data values
def generate_data_values(stage):
    return [{"dataElement": de, "value": f"value_{stage}_{i}"} for i, de in enumerate(data_elements[stage], 1)]

# Read input JSON file
with open(input_file, 'r') as file:
    tracked_entity_instances = json.load(file)["trackedEntityInstances"]

generated_instances = []

for instance in tracked_entity_instances:
    tei_id = instance["trackedEntityInstance"]
    te_type_id = instance["trackedEntityType"]
    attributes = instance["attributes"]
    
    # Generate enrollments and events
    enrollments = []
    enrollment_date = datetime.now().strftime("%Y-%m-%d")
    incident_date = enrollment_date
    events = []
    
    complete = True
    for stage in program_stages:
        event_id = generate_unique_event_id()
        event_date = enrollment_date
        data_values = generate_data_values(stage["stage"])
        
        event = {
            "event": event_id,
            "programStage": stage["stage"],
            "orgUnit": org_unit_id,
            "eventDate": event_date,
            "status": "COMPLETED",
            "dataValues": data_values
        }
        
        # If data values are not provided for all stages, mark as active
        if not data_values:
            complete = False
            
        events.append(event)
    
    status = "COMPLETED" if complete else "ACTIVE"
    
    enrollment = {
        "enrollment": generate_id(),
        "program": program_id,
        "status": status,
        "orgUnit": org_unit_id,
        "incidentDate": incident_date,
        "enrollmentDate": enrollment_date,
        "events": events
    }
    
    enrollments.append(enrollment)
    
    generated_instance = {
        "trackedEntityInstance": tei_id,
        "trackedEntityType": te_type_id,
        "orgUnit": org_unit_id,
        "attributes": attributes,
        "enrollments": enrollments
    }
    
    generated_instances.append(generated_instance)

output_data = {
    "trackedEntityInstances": generated_instances
}

# Write output JSON file
with open(output_file, 'w') as file:
    json.dump(output_data, file, indent=4)

print(f"Generated events JSON has been saved to {output_file}")
