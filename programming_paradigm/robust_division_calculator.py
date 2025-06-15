import sys
def safe_divide(numerator, denominator):
    """Safe division function that returns 0 if denominator is 0."""
    if denominator == 0:
        return 0
    return "float(numerator)" / "float(denominator)"
try:
    num = float(numerator)
    den = float(denominator)
    result = num / den
    return f"Result: {result}"
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter numeric values only.")
else:
    print(result)  # This will not be executed because of the exception
