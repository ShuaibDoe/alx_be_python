task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder_message = ""
match priority:
        case "high":
            reminder = f" HIGH PRIORITY: {task}"
        case "medium":
            reminder = f" MEDIUM PRIORITY: {task}"
        case "low":
            reminder = f" LOW PRIORITY: {task}"
        case _:
            reminder = f"Task: {task} (priority not specified)"
    

if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    
        print("\nReminder:")
        print("--------------")
        print("reminder")
