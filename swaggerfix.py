import json
import sys
import os

# Function to update the JSON data
def update(file_path):
    # Open the JSON file and load the data
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)


    # Get a copy of all the paths
    paths = data['paths'].copy()

    # Iterate over each path in the 'paths' section of the swagger file
    for path, path_data in paths.items():
        # Iterate over each method (GET, POST, etc.) in the current path
        for method, method_data in path_data.items():
            # Check if the method has a 'parameters' key
            if 'parameters' in method_data: 
                # If yes, append a new parameter reference to the 'parameters' list.  In the case of Azure AI Search, it's 'IndexNameParameter'
                # which is defined elsewhere in the Swagger file.
                # TODO: The 'IndexNameParameter' should be replaced with the actual name of the parameter in your Swagger file
                method_data['parameters'].append({"$ref": "#/parameters/IndexNameParameter"})
        # Update the path to include the name of the parameter and replace the old one with this new section.
        # For AI Search, the 'name' value for 'IndexNameParameter' is 'indexName'
        # TODO: The 'indexName' should be replaced with the actual name of the parameter in your Swagger file
        data['paths'][f"/{{indexName}}{path}"] = data['paths'].pop(path)

    # Return the updated data
    return data

# Main function
def main():
    input_file = "searchindex.json"
    # Remove the file extension from the input file name
    base_name = os.path.splitext(input_file)[0]
    # Append '-updated.json' to the base name to get the output file name
    output_file = f"{base_name}-updated.json"

    # Call the update function to get the updated data
    updated_data = update(input_file)

    # Write the updated data to the output file
    with open(output_file, 'w') as json_file:
        json.dump(updated_data, json_file, indent=4)

# If this script is run directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()