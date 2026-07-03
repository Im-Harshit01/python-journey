# A simple program to demonstrate exception handling in Python.


def safe_divide(a, b):
    """Divide two numbers and always report that the attempt finished."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero."
    except TypeError:
        return "Error: please enter numbers only."
    finally:
        print("Division attempt finished.")

    return f"Result: {result}"


def main():
    print("Safe Division Project")
    print("---------------------")

    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
    except ValueError:
        print("Error: invalid number entered.")
        return

    message = safe_divide(first, second)
    print(message)


if __name__ == "__main__":
    main()
