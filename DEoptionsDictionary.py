import pandas as pd

# Replace 'path_to_your_file.csv' with the actual path to your CSV file
file_path = 'C:/Dev/DevRepo/FlaskPythonforMachinelearning/data_elements_with_options.csv'

def create_data_elements_info(file_path):
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Initialize an empty dictionary to store data element information
        data_elements_info = {}
        
        # Iterate over rows in the DataFrame and populate data_elements_info
        for index, row in df.iterrows():
            data_element_id = row['dataElement']
            options = row['options'].split(',') if pd.notnull(row['options']) else None
            
            # Construct the entry for data_elements_info dictionary
            data_elements_info[data_element_id] = {"options": options}
        
        return data_elements_info
    
    except Exception as e:
        print(f"Error creating data elements information from {file_path}: {e}")
        return None

# Example usage
data_elements_info = create_data_elements_info(file_path)

# Print the resulting data_elements_info dictionary
if data_elements_info:
    print("data_elements_info:")
    print(data_elements_info)
else:
    print("Failed to create data_elements_info. Check the file path and format.")