import json
from cli import create_survey, view_survey
from models import Survey

SURVEY_FILE = "surveys.json"

# Load surveys from a file
def load_surveys():
    try:
        with open(SURVEY_FILE, "r") as file:
            data = json.load(file)
            return [Survey.model_validate_json(json.dumps(item)) for item in data]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading survey data. Starting with an empty list.")
        return []

# Save surveys to a file
def save_surveys(surveys):
    with open(SURVEY_FILE, "w") as file:
        file.write(json.dumps([survey.model_dump() for survey in surveys], indent=4))

def main():
    surveys = load_surveys()

    while True:
        print("\nChoose an action:")
        print("1. Create a new survey")
        print("2. View all surveys")
        print("3. View survey details")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            survey = create_survey()
            surveys.append(survey)
            save_surveys(surveys)
            print(f"Survey '{survey.title}' created successfully!")
        elif choice == "2":
            if not surveys:
                print("No surveys available.")
            else:
                for i, survey in enumerate(surveys, start=1):
                    print(f"{i}. {survey.title}")
        elif choice == "3":
            if not surveys:
                print("No surveys available.")
            else:
                for i, survey in enumerate(surveys, start=1):
                    print(f"{i}. {survey.title}")
                try:
                    survey_index = int(input("Enter the number of the survey to view: ")) - 1
                    if 0 <= survey_index < len(surveys):
                        view_survey(surveys[survey_index])
                    else:
                        print("Invalid selection. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == "4":
            save_surveys(surveys)
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
