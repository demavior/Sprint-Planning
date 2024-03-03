def input_positive_integer(prompt):
    # Loop until a valid integer greater than 0 is entered
    while True:
        try:
            # Attempt to convert user input to an integer
            value = int(input(prompt))
            # Check if the value is less than 0
            if value < 0:
                print("Invalid input. Please enter an integer greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer greater than 0.")

def get_total_hours(sprint_days, num_members):
    
    min_total_hours=0
    max_total_hours=0

    # For each team member
    for x in range(num_members):
        
        # Get days off 
        days_off = input_positive_integer(f"Enter days off for member {x + 1}: ")
        # Get hours for scrum activities
        hours_scrum = input_positive_integer(f"Enter total hours committed to scrum activities for member {x + 1}: ")
        # Get the range of available hours per day from the user
        hours_range = input(f"Enter available hours per day for member {x + 1} (e.g., '5-8'): ")
        # Split the hours range
        hours_range = hours_range.split('-')
        
        # Get the minimum and the maximum hours
        min_hours = int(hours_range[0])
        max_hours = int(hours_range[1])
        
        # Calculate total hours within the range
        min_total_hours += (sprint_days - days_off) * min_hours - hours_scrum
        max_total_hours += (sprint_days - days_off) * max_hours - hours_scrum

    return f"{min_total_hours} - {max_total_hours}"

def calculate_team_capacity():
    # Get the number of sprint days from user input
    sprint_days = input_positive_integer("Enter number of sprint days: ")
    # Get the number of team members from user input
    num_members = input_positive_integer("Enter number of team members: ")
    # Get team total hours
    team_hours = get_total_hours(sprint_days, num_members)
    print("Team Effort-Hour Capacity:", team_hours)

if __name__ == "__main__":
    calculate_team_capacity() 