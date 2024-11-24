from cli import create_survey, add_question, view_survey, export_survey

def main():
    survey = create_survey()
    while True:
        print("\nChoose an action:")
        print("1. Add question")
        print("2. View survey")
        print("3. Export survey")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_question(survey)
        elif choice == "2":
            view_survey(survey)
        elif choice == "3":
            export_survey(survey)
        elif choice == "4":
            print("Exiting Survey Builder. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
