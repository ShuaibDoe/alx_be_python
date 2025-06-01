def main():
    print("Daily Task Reminder\n")
    
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    print("\nReminder: ", end='')
    
    if priority == "high":
            if time_bound == "yes":
                print(f"'{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"'{task}' is a high priority task. You should focus on this soon.")
                
    elif priority == "medium":
            if time_bound == "yes":
                print(f"'{task}' is a medium priority task that should be completed today.")
            else:
                print(f"'{task}' is a medium priority task. Consider completing it this week.")
                
    elif priority == "low":
            if time_bound == "yes":
                print(f"Note: '{task}' is a low priority task but has a deadline today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
                
    else:
            print("Invalid priority level entered. Please use high, medium, or low.")

if _name_ == "_main_":
    while True:
        main()
        another = input("\nWould you like to set another reminder? (yes/no): ").lower()
        if another != "yes":
            print("\nHave a productive day!")
            break
