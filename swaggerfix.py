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

    # Iterate over each path in the data and update it
    for path, path_data in paths.items():
        for method, method_data in path_data.items():
            if 'parameters' in method_data:
                method_data['parameters'].append({"$ref": "#/parameters/IndexNameParameter"})
        # Append '/{indexname}' to the path
        data['paths'][f"/{{indexName}}{path}"] = data['paths'].pop(path)
    



    # for path, path_data in paths.items():
    #     if not path.startswith(f"/{{indexname}}"):
    #         data['paths'][f"/{{indexname}}{path}"] = data['paths'].pop(path)

    #         for method, method_data in path_data.items():
    #             if 'parameters' in method_data:
    #                 method_data['parameters'].append({"$ref": "#/parameters/IndexNameParameter"})

    # data['paths'].update(paths)
        
        
    
    #Get the number of path elements
    # path_elements = len(data['paths'])
    # paths = data['paths']
    # for i in range(path_elements):
    #     # Get the path for the index
    #     path = paths[i]
    #     # Append '/{indexname}' to the path
    #     paths[i] = f"/{{indexname}}/{path}"
                

                
    # update all path
    # Iterate over each path in the data
    
    # for path in data['paths']:
    #     # Append '/{indexname}' to the path
    #     #data['paths'][path] = f"/{{indexname}}/{path}"
    #     #if path begins with /indexname, continue
    #     if path.startswith("{{/indexname}}"):
    #         continue
    #     new_path = f"/{{indexname}}{path}"  # replace with your new path name
    #     data['paths'][new_path] = data['paths'].pop(path)
    
    


    # Return the updated data
    return data

# Main function
def main():
    # Get the input file name from the command line arguments
    input_file = "searchindex.json" #sys.argv[1]
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