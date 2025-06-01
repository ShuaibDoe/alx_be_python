task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

while priority not in ['high', 'medium', 'low']:
        print("Invalid priority. Please enter high, medium, or low.")
        priority = input("Priority (high/medium/low): ").lower()

while time_bound not in ['yes', 'no']:
        print("Invalid input. Please enter yes or no.")
        time_bound = input("Is it time-bound? (yes/no): ").lower()

message = ""
    
if priority == 'high':
        message = f"'{task}' is a high priority task"
        if time_bound == 'yes':
            message += " that requires immediate attention today!"
        else:
            message += ". You should address this soon."
        print(f"\nReminder: {message}")
else:
        if priority == 'medium':
            message = f"'{task}' is a medium priority task"
            if time_bound == 'yes':
                message += " that should be completed soon."
            else:
                message += ". Try to complete it this week."
        elif priority == 'low':
            message = f"'{task}' is a low priority task"
            if time_bound == 'yes':
                message += " with a flexible deadline."
            else:
                message += ". Consider completing it when you have free time."
        print(f"\nNote: {message}")




