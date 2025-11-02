import sys

def safe_divide(numerator, denominator):
    """
    Performs division of numerator by denominator with robust error handling.

    Args:
        numerator (str or float): The numerator.
        denominator (str or float): The denominator.

    Returns:
        str: Result of division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def main():
    if len(sys.argv) != 3:
        print("Usage: python calculator.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
