from survey_builder.cli import create_survey, add_question, view_survey
from survey_builder.utils import export_survey

def main():
    survey = create_survey()
    while True:
        action = input("Choose an action (add_question, view_survey, export, quit): ").strip()
        if action == "add_question":
            add_question(survey)
        elif action == "view_survey":
            view_survey(survey)
        elif action == "export":
            export_survey(survey)
        elif action == "quit":
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()
