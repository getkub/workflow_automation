import os
import shutil
from github import Github

# Directory paths
main_workflows_directory = 'n8n-workflows/main_workflows'
subworkflows_directory = 'n8n-workflows/subworkflows'

# Zip the directory structure
shutil.make_archive('n8n-workflows', 'zip', 'n8n-workflows')

# Upload the zip file to GitHub or a similar location
github_access_token = 'YOUR_GITHUB_ACCESS_TOKEN'
repository_name = 'your-repository-name'
zip_file_path = 'n8n-workflows.zip'

g = Github(github_access_token)
repo = g.get_repo(repository_name)

# Create a new release
release = repo.create_git_release(tag='v1.0', name='n8n workflows v1.0', message='Release v1.0')

# Upload the zip file as an asset to the release
release.upload_asset(zip_file_path, label='n8n-workflows.zip')

# Clean up the temporary zip file
os.remove(zip_file_path)
shutil.rmtree('n8n-workflows')
