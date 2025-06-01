task = str(input("Enter your task: ")).lower()
priority = str(input("Enter priority (high/medium/low): ")).lower()
time_bound = str(input("Is this task time-bound? (yes/no): ")).lower()
    
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
    
        print("\nYour reminder:")
        print("--------------")
        print("reminder")
