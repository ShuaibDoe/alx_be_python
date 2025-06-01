task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

while priority not in ['high', 'medium', 'low']:
        print("Invalid priority. Please enter high, medium, or low.")
        priority = input("Priority (high/medium/low): ").lower()

while time_bound not in ['yes', 'no']:
        print("Invalid input. Please enter yes or no.")
        time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = ""
    
match priority:
        case 'high':
            reminder = f"'{task}' is a high priority task"
            if time_bound == 'yes':
                reminder += " that requires immediate attention today!"
            else:
                reminder += ". You should address this soon."
        case 'medium':
            reminder = f"Note: '{task}' is a medium priority task"
            if time_bound == 'yes':
                reminder += " that should be completed by the end of the day."
            else:
                reminder += ". Try to complete it this week."
        case 'low':
            reminder = f"Note: '{task}' is a low priority task"
            if time_bound == 'yes':
                reminder += " with a flexible deadline."
            else:
                reminder += ". Consider completing it when you have free time."

print("\n" + reminder)

