from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time"""
    current_datetime = datetime.now()
    print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days_to_add):
    """Calculate a future date by adding days to today"""
    future_datetime = datetime.now() + timedelta(days=days_to_add)
    return future_datetime.strftime("%Y-%m-%d")

# Main program
if __name__ == "__main__":
    display_current_datetime()  # Show current datetime
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(days)
    print(f"Date {days} days from now will be: {future_date.strftime}")
