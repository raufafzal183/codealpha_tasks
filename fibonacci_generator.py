def generate_fibonacci(n):
    # Start with an empty list
    fibonacci_series = []
    
    # First two Fibonacci numbers
    a, b = 0, 1
    
    # Generate n terms
    for i in range(n):
        fibonacci_series.append(a)
        print(f"Term {i + 1}: {a}")
        a, b = b, a + b  # Move to next term
    
    return fibonacci_series

def main():
    print("=== Fibonacci Series Generator ===")
    
    try:
        # Ask user to input number of terms
        terms = int(input("Enter the number of Fibonacci terms to generate: "))
        
        # Validate input
        if terms <= 0:
            print("Please enter a positive number.")
        else:
            # Generate and print the series
            series = generate_fibonacci(terms)
            print("\nFull Fibonacci Series:")
            print(series)
    
    except ValueError:
        # Handle invalid input (like strings)
        print("Invalid input. Please enter a valid integer.")

# Start the program
if __name__ == "__main__":
    main()
