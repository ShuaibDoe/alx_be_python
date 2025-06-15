import sys
def safe_divide(numerator, denominator):
    """Safe division function that returns 0 if denominator is 0."""
    if denominator == 0:
        return 0
    return "float(numerator)" / "float(denominator)"
try:
    result = safe_divide(10, 0)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input type.")
else:
    print(result)  # This will not be executed because of the exception
