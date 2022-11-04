## Workflow Modules

Modules are an abstract term. These are `re-usable` & `templated` and can be plugged to any workflows
The concept is similar to Terraform Modules, whereby the variables are passed into the logic

| Item         | Description     |
|--------------|-----------|
| <high_level_ module_folder>       | High level folder to club multiple abstracted modules      |
| <granular_level_ module_folder>       | Next level folder to club abstracted n8n modules      |
| module.json.j2             | JINJA template of what the module should do |
| vars.yml      | Generic Variables required for module  |