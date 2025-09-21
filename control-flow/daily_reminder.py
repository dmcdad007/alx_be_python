# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
    case _:
        reminder = f"Note: '{task}' has an unknown priority."

# Check if task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
elif time_bound == "no":
    reminder += " Consider completing it when you have free time."

# Print customized reminder
print(reminder)

