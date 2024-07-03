import toml
import re

def extract_dependencies(lockfile_path, output_path):
    # Load the lock file
    with open(lockfile_path, 'r') as f:
        lock_data = toml.load(f)

    dependencies = lock_data['package']

    # Regular expression to match the local file paths and replace them with the version specifier
    local_path_pattern = re.compile(r' @ file:///.*')

    with open(output_path, 'w') as f:
        for dep in dependencies:
            name = dep['name']
            version = dep['version']
            dep_string = f"{name}=={version}"
            dep_string = re.sub(local_path_pattern, '', dep_string)
            f.write(f"{dep_string}\n")

# Specify the path to your pdm.lock file and the output requirements.txt file
lockfile_path = 'pdm.lock'
output_path = 'requirements.txt'

extract_dependencies(lockfile_path, output_path)
