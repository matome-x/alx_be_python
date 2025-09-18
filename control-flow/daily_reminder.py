# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Base reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Add time-bound modification
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no" and priority in ["medium", "low"]:
    reminder += ". Consider completing it when you have free time."

# Print the reminder
print(reminder)
