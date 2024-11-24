from models import Survey, Question
from pydantic import ValidationError

def create_survey():
    title = input("Enter survey title: ")
    description = input("Enter survey description: ")
    return Survey(title=title, description=description)

def add_question(survey: Survey):
    try:
        question_text = input("Enter the question text: ")
        question_type = input("Enter the question type (multiple_choice, rating, text): ")

        if question_type == "multiple_choice":
            choices = input("Enter choices (comma-separated): ").split(",")
            question = Question(question_text=question_text, question_type=question_type, choices=choices)

        elif question_type == "rating":
            min_scale = int(input("Enter the minimum rating: "))
            max_scale = int(input("Enter the maximum rating: "))
            question = Question(question_text=question_text, question_type=question_type, rating_scale=(min_scale, max_scale))

        elif question_type == "text":
            question = Question(question_text=question_text, question_type=question_type)

        else:
            print("Invalid question type. Please try again.")
            return

        survey.questions.append(question)
        print("Question added successfully!")

    except ValidationError as e:
        print("Error adding question:")
        print(e)

def view_survey(survey: Survey):
    print(survey.json(indent=4))

def export_survey(survey: Survey, file_path: str = "survey.json"):
    with open(file_path, "w") as file:
        file.write(survey.json(indent=4))
    print(f"Survey exported to {file_path}")
