from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")
    return current_date  # Return the current date for future use

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    # Prompt user for number of days
    days_to_add = int(input("Enter number of days to add: "))
    # Calculate future date
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in "YYYY-MM-DD" format
    print(f"Future Date: {future_date.strftime('%Y-%m-%d')}")

# Main program flow
if __name__ == "__main__":
    # Display current date/time and store current date
    current_date = display_current_datetime()
    # Calculate and display future date
    calculate_future_date(current_date)
