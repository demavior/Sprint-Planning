def input_positive_integer(prompt):
    # Loop until a valid integer greater than 0 is entered
    while True:
        try:
            # Attempt to convert user input to an integer
            value = int(input(prompt))
            # Check if the value is less than or equal to 0
            if value <= 0:
                print("Invalid input. Please enter an integer greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer greater than 0.")

def get_total_hours(sprint_days, num_members):
    max_total_hours=0
    min_total_hours=0
    total_hours=0
    for x in range(num_members):
        days_off = int(input(f"Enter days off for member {x + 1}: "))
        hours_scrum = int(input(f"Enter hours committed to scrum activities for member {x + 1}: "))
        hours_available = int(input(f"Enter available hours per day for member {x + 1}: "))
        total_hours += (sprint_days - days_off) * (hours_available - hours_scrum)
        
    return total_hours

def calculate_team_capacity():
    # Get the number of sprint days from user input
    sprint_days = input_positive_integer("Enter number of sprint days: ")
    # Get the number of team members from user input
    num_members = input_positive_integer("Enter number of team members: ")
    # Get team total hours
    team_hours = get_total_hours(sprint_days, num_members)

if __name__ == "__main__":
    calculate_team_capacity() 