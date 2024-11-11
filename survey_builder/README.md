# Survey Builder CLI

The Survey Builder CLI is a command-line tool designed to help users create and manage surveys with various question types, such as `multiple-choice`, `rating`, and `text-based questions`. This project is built using Python, with Pydantic models to enforce data validation, and it supports basic survey creation, question addition, and export functionality.

Features
* Create a Survey: Define a title and description for each survey.  
* Add Questions: Add multiple-choice, rating, and text questions with built-in validation.
* Export Surveys: Export surveys to a JSON file for storage and future use.

# Repo Structure:

$->
survey_builder/
├── survey_builder/
│   ├── __init__.py
│   ├── __main__.py           # Entry point for the CLI
│   ├── models.py             # Pydantic models for surveys and questions
│   ├── cli.py                # CLI functions for user interaction
│   ├── utils.py              # Utility functions for import/export
├── tests/
│   ├── __init__.py
│   ├── test_models.py        # Unit tests for models
│   ├── test_cli.py           # Unit tests for CLI functions
├── README.md                 # Project description and usage instructions
├── pyproject.toml            # Poetry configuration file
└── survey.json               # Example JSON file for exporting surveys
