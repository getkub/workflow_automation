import os
import shutil

# Directory paths
template_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
subworkflows_directory = '/tmp/n8n/workflow/subworkflows'

# Cleanup the subworkflows directory
shutil.rmtree(subworkflows_directory, ignore_errors=True)
os.makedirs(subworkflows_directory, exist_ok=True)

# Copy template code files to subworkflow directories
def copy_code_files(template_directory, subworkflows_directory):
    # Get the list of template code files
    template_files = os.listdir(template_directory)

    # Copy each template code file to the respective subworkflow directory
    for template_file in template_files:
        template_file_path = os.path.join(template_directory, template_file)
        subworkflow_directory = os.path.join(subworkflows_directory, os.path.splitext(template_file)[0])

        # Create the subworkflow directory if it doesn't exist
        os.makedirs(subworkflow_directory, exist_ok=True)

        # Copy the template code file to the subworkflow directory
        shutil.copy2(template_file_path, subworkflow_directory)

# Copy template code files to subworkflow directories
copy_code_files(template_directory, subworkflows_directory)
