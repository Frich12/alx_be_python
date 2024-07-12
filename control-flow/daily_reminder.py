# daily_reminder.py

# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Print initial reminder message
print("\nReminder:")

# Process the task based on priority and time sensitivity
match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. Consider completing it as soon as possible.")
    case 'medium':
        if time_bound == 'yes':
            print(f"'{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a medium priority task. Plan to complete it soon.")
    case 'low':
        if time_bound == 'yes':
            print(f"'{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Priority level '{priority}' is not recognized.")
