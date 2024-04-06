# Fibonacci Sequence
def generate_fibonacci(num_terms):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two terms
    #Checks the input is Positive Integer:
    if num_terms <= 0:
        print("Please enter a positive integer for the number of terms.")
        return
    #Checks the input is 1 term:
    elif num_terms == 1:
        print("Fibonacci sequence up to 1 term:", fibonacci_sequence[:1])
        return
    #Checks the input is 2 term:
    elif num_terms == 2:
        print("Fibonacci sequence up to 2 terms:", fibonacci_sequence)
        return

    # Generate Fibonacci sequence up to num_terms
    for _ in range(2, num_terms):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    print("Fibonacci sequence up to", num_terms, "terms:", fibonacci_sequence)


def main():
    num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    generate_fibonacci(num_terms)


if __name__ == "__main__":
    main()
