import json
from survey_builder.models import Survey

def export_survey(survey: Survey, filename="survey.json"):
    with open(filename, "w") as f:
        json.dump(survey.dict(), f, indent=4)
    print(f"Survey exported to {filename}")

def import_survey(filename="survey.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return Survey(**data)
