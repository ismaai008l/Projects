from models import Survey

def create_survey():
    """Create a new survey."""
    title = input("Enter survey title: ")
    description = input("Enter survey description (optional): ")
    return Survey(title=title, description=description)

def view_survey(survey: Survey):
    """View the details of a survey."""
    print("\nSurvey Details:")
    print(f"Title: {survey.title}")
    print(f"Description: {survey.description or 'No description provided'}")
    if not survey.questions:
        print("No questions in this survey yet.")
    else:
        print("Questions:")
        for i, question in enumerate(survey.questions, start=1):
            print(f"  {i}. {question.question_text} ({question.question_type})")
