# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority level (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes or no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Note: '{task}' is a low priority task."
    case _:
        reminder = f"Unspecified Priority: '{task}' has no clear urgency."

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"
elif time_bound == "no":
    reminder += " Consider completing it when you have free time"

    print(reminder)


