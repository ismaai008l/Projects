# survey_builder/__main__.py
import json
from survey_builder.models import Survey, MultipleChoiceQuestion, RatingQuestion, TextQuestion

def create_survey():
    title = input("Enter survey title: ")
    description = input("Enter survey description: ")
    return Survey(title=title, description=description)

def add_question(survey):
    question_type = input("Choose question type (multiple_choice, rating, text): ").strip()
    question_text = input("Enter the question text: ")

    if question_type == "multiple_choice":
        choices = input("Enter choices (comma-separated): ").split(',')
        survey.questions.append(MultipleChoiceQuestion(question_text=question_text, choices=choices))
    elif question_type == "rating":
        min_rating = int(input("Enter minimum rating: "))
        max_rating = int(input("Enter maximum rating: "))
        survey.questions.append(RatingQuestion(question_text=question_text, min_rating=min_rating, max_rating=max_rating))
    elif question_type == "text":
        survey.questions.append(TextQuestion(question_text=question_text))
    else:
        print("Invalid question type")

def main():
    survey = create_survey()
    while True:
        action = input("Choose an action (add_question, view_survey, export, quit): ").strip()
        if action == "add_question":
            add_question(survey)
        elif action == "view_survey":
            print(survey.json(indent=4))
        elif action == "export":
            with open("survey.json", "w") as f:
                json.dump(survey.dict(), f, indent=4)
            print("Survey exported to survey.json")
        elif action == "quit":
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()
