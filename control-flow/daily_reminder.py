# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority level (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes or no): ").lower()

# Process the task based on priority
reminder = ""

match priority:
    case "high":
        reminder = f"🔴 High Priority: '{task}' needs your urgent attention."
    case "medium":
        reminder = f"🟠 Medium Priority: '{task}' should be completed soon."
    case "low":
        reminder = f"🟢 Low Priority: '{task}' can be done at your convenience."
    case _:
        reminder = f"⚪ Unspecified Priority: '{task}' has no clear urgency."

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"

# Display the customized reminder with a loop for emphasis
for i in range(1, 2):  # Loop runs once to demonstrate control flow
    print("\nYour Daily Reminder:")
    print(reminder)
