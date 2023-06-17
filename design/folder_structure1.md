```
/n8n
├── config
│   ├── production
│   │   └── values
│   │       └── api_key.yml
│   └── preproduction
│       └── values
│           └── api_key.yml
└── subworkflows
│   ├── common
│   │   └── logger.yml
│   ├── data_ingestion
│   │   └── load_data.yml
│   └── data_processing
│       ├── clean_data.yml
│       └── analyze_data.yml
└── workflows
    ├── main.yml
    └── user_facing
        └── greet_user.yml
```