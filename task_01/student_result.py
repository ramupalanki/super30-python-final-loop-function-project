"""Student Result Management System."""

def accept_marks(subject_count):
    """Accept and return marks for each subject."""
    marks = []
    for i in range(1, subject_count + 1):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    return marks


def calculate_total(marks):
    """Calculate total marks without using sum()."""
    total = 0
    for mark in marks:
        total += mark
    return total


def calculate_percentage(total, subject_count):
    """Calculate percentage from total marks."""
    return total / subject_count


def assign_grade(percentage):
    """Assign a grade based on percentage."""
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 50:
        return "D"
    return "F"


def determine_result(marks):
    """Determine pass/fail using a 35-mark minimum per subject."""
    for mark in marks:
        if mark < 35:
            return "FAIL"
    return "PASS"


def display_result(name, marks, total, percentage, grade, result):
    """Display the complete student result."""
    print("\n===== STUDENT RESULT =====")
    print(f"Student: {name}")
    for index, mark in enumerate(marks, start=1):
        print(f"Subject {index}: {mark:.2f}")
    print(f"Total: {total:.2f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")


def main():
    """Run the student result program."""
    print("Student Result Management System")
    name = input("Enter student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    while True:
        try:
            subject_count = int(input("Enter number of subjects: "))
            if subject_count > 0:
                break
            print("Enter at least one subject.")
        except ValueError:
            print("Please enter a whole number.")

    marks = accept_marks(subject_count)
    total = calculate_total(marks)
    percentage = calculate_percentage(total, subject_count)
    grade = assign_grade(percentage)
    result = determine_result(marks)
    display_result(name, marks, total, percentage, grade, result)


if __name__ == "__main__":
    main()
