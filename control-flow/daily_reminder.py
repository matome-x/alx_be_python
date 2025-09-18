# Prompt the user for task details
task = input("Enter a task description: ")
priority = input("Enter the task's priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Initialize the reminder message based on priority
match priority:
    case "high":
        reminder = f"Reminder: Your task '{task}' has HIGH priority"
    case "medium":
        reminder = f"Reminder: Your task '{task}' has MEDIUM priority"
    case "low":
        reminder = f"Reminder: Your task '{task}' has LOW priority"
    case _:
        reminder = f"Reminder: Your task '{task}' has an UNKNOWN priority"

# Modify message if the task is time-bound
if time_bound == "yes":
    reminder += " and requires immediate attention today!"

# Print the customized reminder
print(reminder)
