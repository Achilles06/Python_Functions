def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """
    Returns the result of dividing the first number by the second.
    Assumes the second number is not zero.
    """
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero!")

def power(base, exponent):
    """Returns the result of raising the base to the given exponent."""
    return base ** exponent

def main():
    print("Welcome to the Arithmetic Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /, ^): ")

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    elif operation == "^":
        result = power(num1, num2)
    else:
        print("Invalid operation. Please choose +, -, *, /, or ^.")
        return

    print(f"Result: {result:.2f}")

if __name__ == "__main__":
    main()
