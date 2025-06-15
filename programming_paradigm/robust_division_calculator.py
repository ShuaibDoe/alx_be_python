import sys
def safe_divide(numerator, denominator):
    """Safe division function that returns 0 if denominator is 0."""
    if denominator == 0:
        return 0
    return numerator / denominator
try:
    result = safe_divide(10, 0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input type.")
else:
    print(result)  # This will not be executed because of the exception