import os
import yaml

def create_file_and_directories(file_path, content):
    # Get the directory path from the full file path
    directory = os.path.dirname(file_path)

    # Check if the directory exists, and if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write the content to the file
    with open(file_path, "w") as f:
        f.write(content)

def write_yaml(file_path, content):
    # Get the directory path from the full file path
    directory = os.path.dirname(file_path)

    # Check if the directory exists, and if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Write the content to the file
    with open(file_path, "w") as f:
        yaml.dump(content, f, default_flow_style=False, sort_keys=False)