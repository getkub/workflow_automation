## workflow_automation
Creating Workflow automation using n8n and Entirely based on dynamic templates


| Item         | Description     |
|--------------|-----------|
| ansible_playbooks     | Build & Deployment Playbooks      |
| integrations          | Various integrations and vault      |
| use_cases             | Detailed UseCases  |
| workflow_modules      | Abstracted workflow modules  |


## Operations

- To run
```
ansible-playbook -e "env=prod wf=wf00" generate_workflow.yml
```