def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep shining 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good effort! You can do even better 😊"
    elif 60 <= marks <= 69:
        return "D", "You passed, but work harder 💪"
    else:
        return "F", "Don't give up! Learn and try again 📘"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print(" Marks must be between 0 and 100. Try again.")
        except ValueError:
            print(" Please enter a valid number.")


def main():
    print("Student Grade Calculator")
    print("---------------------------")

    name = input("Enter student name: ")
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n RESULT FOR", name.upper())
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)


if __name__ == "__main__":
    main()
