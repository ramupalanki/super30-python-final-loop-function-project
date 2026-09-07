"""Prime Number Analyzer."""

def is_prime(number):
    """Return True when number is prime."""
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def find_primes(start, end):
    """Return all prime numbers in the inclusive range."""
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes


def count_primes(primes):
    """Return the number of primes."""
    count = 0
    for _ in primes:
        count += 1
    return count


def calculate_prime_sum(primes):
    """Calculate the sum of primes manually."""
    total = 0
    for prime in primes:
        total += prime
    return total


def display_largest_prime(primes):
    """Display the largest prime found."""
    if not primes:
        print("No prime numbers found.")
    else:
        largest = primes[0]
        for prime in primes:
            if prime > largest:
                largest = prime
        print(f"Largest prime: {largest}")


def main():
    """Run the prime number analyzer."""
    print("===== PRIME NUMBER ANALYZER =====")

    while True:
        try:
            start = int(input("Enter start of range: "))
            end = int(input("Enter end of range: "))
            if start <= end:
                break
            print("Start must be less than or equal to end.")
        except ValueError:
            print("Please enter valid integers.")

    primes = find_primes(start, end)

    print(f"Prime numbers: {primes}")
    print(f"Prime count: {count_primes(primes)}")
    print(f"Prime sum: {calculate_prime_sum(primes)}")
    display_largest_prime(primes)


if __name__ == "__main__":
    main()
