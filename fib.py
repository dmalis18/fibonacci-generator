"""Fibonacci Number Generator."""

def main()
    """Takes in user input, returns Fibonacci Numbers."""
    num_terms = input("Enter number of fibonacci terms: ")
    
    # Validates input - checks that the input is a non-negative number
    valid = num_terms.isnumeric()
    if valid:
        a, b = 1,1

        # Loop iterates for the requested number of terms
        for i in range(0, int(num_terms)):
            print(a)
            a, b = b, a+b
            i += 1
    else:
        print("Invalid input. Input must be a numeric value")

main()

