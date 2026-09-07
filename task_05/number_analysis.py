"""Number Analysis Tool."""

def analyze_numbers(numbers):
    """Return largest, smallest, total, average, and number counts.

    This function intentionally does not use min(), max(), or sum().
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    largest = numbers[0]
    smallest = numbers[0]
    total = 0
    even_count = 0
    odd_count = 0
    positive_count = 0
    negative_count = 0

    for number in numbers:
        total += number

        if number > largest:
            largest = number
        if number < smallest:
            smallest = number

        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1

    average = total / len(numbers)

    return (
        largest,
        smallest,
        total,
        average,
        even_count,
        odd_count,
        positive_count,
        negative_count,
    )


def main():
    """Run the number analysis tool."""
    print("===== NUMBER ANALYSIS TOOL =====")
    while True:
        try:
            count = int(input("How many numbers do you want to enter? "))
            if count > 0:
                break
            print("Enter at least one number.")
        except ValueError:
            print("Please enter a whole number.")

    numbers = []
    for index in range(1, count + 1):
        while True:
            try:
                numbers.append(int(input(f"Enter number {index}: ")))
                break
            except ValueError:
                print("Please enter a valid integer.")

    result = analyze_numbers(numbers)
    labels = [
        "Largest", "Smallest", "Total", "Average",
        "Even count", "Odd count", "Positive count", "Negative count"
    ]

    print("\n===== ANALYSIS =====")
    for label, value in zip(labels, result):
        print(f"{label}: {value}")


if __name__ == "__main__":
    main()
