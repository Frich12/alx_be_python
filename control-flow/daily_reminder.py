task = input ("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input (" Is it time-bound? (yes/no):")

print("\nReminder:")
match priority:
    case 'high':
        if time_bound.lower() == 'yes' :
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high prority task. Consider completing it as soon as possible.") 
    case 'medium':
        if time_bound.lower() == 'yes' :
            print(f"'{task}'is a medium priority task that requires immediate attention today! ")  
        else:
            print(f"'{task}' is a medium prority task. Consider completing it as soon as possible.") 
    case 'low':
        if time_bound.lower() == 'yes' :
            print(f"'{task}'is a low priority task that requires immediate attention today! ")     
        else:
            print(f"'{task}' is a low prority task. Consider completing it as soon as possible.")

    case _:
        print(f"Priority level '{priority}' is not recognized.")        

            