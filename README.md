## workflow_automation
Creating Workflow automation using n8n and Entirely based on dynamic templates

The aim is to have enterprise level n8n workflow system. 
The advantages are
- All workflow generated from code-base
- Develop in UI anywhere and then capture the code as a template into version control.
- Build & deployment into TEST & PROD systems are done automatically thus getting consistency
- Single point of change. For instance change one sub-module and ALL the use-cases could be changed at once
- No requirement for end-user to have edit access to PROD UI
- Can be automated to CI/CD systems, so n8n code deployment can be done in devops methodology


| Item         | Description     |
|--------------|-----------|
| ansible_playbooks     | Build & Deployment Playbooks      |
| integrations          | Various integrations and vault      |
| use_cases             | Detailed UseCases  |
| workflow_modules      | Abstracted workflow modules  |