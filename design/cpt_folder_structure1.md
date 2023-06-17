```
n8n-workflows/
├── main_workflows/
│   ├── email_security/
│   │   ├── email_security_workflow.json
│   │   └── values/
│   │       ├── production_values.json
│   │       ├── preproduction_values.json
│   │       └── ...
│   ├── ticket_management/
│   │   ├── ticket_management_workflow.json
│   │   └── values/
│   │       ├── production_values.json
│   │       ├── preproduction_values.json
│   │       └── ...
│   ├── data_privacy/
│   │   ├── data_privacy_workflow.json
│   │   └── values/
│   │       ├── production_values.json
│   │       ├── preproduction_values.json
│   │       └── ...
│   ├── misp_threat_sharing/
│   │   ├── misp_threat_sharing_workflow.json
│   │   └── values/
│   │       ├── production_values.json
│   │       ├── preproduction_values.json
│   │       └── ...
│   ├── cortex/
│   │   ├── cortex_workflow.json
│   │   └── values/
│   │       ├── production_values.json
│   │       ├── preproduction_values.json
│   │       └── ...
│   └── ...
├── subworkflows/
│   ├── email_analysis/
│   │   ├── email_analysis_workflow.json
│   │   └── values/
│   │       ├── production_values.json
│   │       ├── preproduction_values.json
│   │       └── ...
│   ├── ticket_creation/
│   │   ├── ticket_creation_workflow.json
│   │   └── values/
│   │       ├── production_values.json
│   │       ├── preproduction_values.json
│   │       └── ...
│   ├── data_classification/
│   │   ├── data_classification_workflow.json
│   │   └── values/
│   │       ├── production_values.json
│   │       ├── preproduction_values.json
│   │       └── ...
│   ├── misp_integration/
│   │   ├── misp_integration_workflow.json
│   │   └── values/
│   │       ├── production_values.json
│   │       ├── preproduction_values.json
│   │       └── ...
│   ├── cortex_integration/
│   │   ├── cortex_integration_workflow.json
│   │   └── values/
│   │       ├── production_values.json
│   │       ├── preproduction_values.json
│   │       └── ...
│   └── ...
└── nodes/
    ├── email_notification/
    │   ├── email_notification_definition.json
    │   └── ...
    ├── data_transformation/
    │   ├── data_transformation_definition.json
    │   └── ...
    ├── slack_integration/
    │   ├── slack_integration_definition.json
    │   └── ...
    └── ...

```