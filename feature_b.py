def validate_hours_input(prompt):
    while True:
        input_string = input(prompt)
        # Check if the input contains a hyphen (indicating a range)
        if '-' in input_string:
            # Split the input string into low and high values
            hours_range = input_string.split('-')
            # Validate low and high values
            try:
                if len(hours_range) > 2:
                    print("The range should contain only 2 values")
                    continue
                low_value = int(hours_range[0])
                high_value = int(hours_range[1])
                # Check if values are within the valid range (0-24)
                if 0 <= low_value < 24 and 0 <= high_value < 24:
                    return [low_value, high_value]
                else:
                    print("Invalid input. Hours should be positive less than 24.")
            except ValueError:
                print("Invalid input. Please enter integers separated by a hyphen.")
        else:
            # Check if the input is an integer
            try:
                hours = int(input_string)
                # Check if the value is less than 24
                if 0 <= hours < 24:
                    return [hours]
                else:
                    print("Invalid input. Hours should be positive less than 24.")
            except ValueError:
                print("Invalid input. Please enter a valid integer or range (e.g., '5-8').")

def input_positive_integer(prompt):
    # Loop until a valid integer greater than 0 is entered
    while True:
        try:
            # Attempt to convert user input to an integer
            value = int(input(prompt))
            # Check if the value is less than 0
            if value < 0:
                print("Invalid input. Please enter a positive integer value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a positive integer value.")

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
        hours_range = validate_hours_input(f"Enter available hours per day for member {x + 1} (e.g., '5-8'): ")
        
        # Get the minimum and the maximum hours
        min_hours = int(hours_range[0])
        if len(hours_range) == 1:
            max_hours = int(hours_range[0])
        else:
            max_hours = int(hours_range[1])
        
        # Calculate total min and max per member
        min_hours = (sprint_days - days_off) * min_hours - hours_scrum
        if min_hours < 0:
            min_hours = 0
        max_hours = (sprint_days - days_off) * max_hours - hours_scrum
        if max_hours < 0:
            max_hours = 0
        
        print(" ")
        print(f"Member {x+1} Available effort hours: {min_hours} - {max_hours}")
        print(" ")
        
        # Calculate total hours within the range
        min_total_hours += min_hours
        max_total_hours += max_hours

    return f"{min_total_hours} - {max_total_hours}"

def calculate_team_capacity():
    # Get the number of sprint days from user input
    sprint_days = input_positive_integer("Enter number of sprint days: ")
    if sprint_days == 0:
        num_members = 0
    else:
        # Get the number of team members from user input
        num_members = input_positive_integer("Enter number of team members: ")
    # Get team total hours
    team_hours = get_total_hours(sprint_days, num_members)
    
    print(" ")
    print("Team Effort-Hour Capacity:", team_hours)
    print(" ")

if __name__ == "__main__":
    calculate_team_capacity() 