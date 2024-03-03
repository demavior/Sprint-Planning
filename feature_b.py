def calculate_team_capacity():
    # While there is not a correct input
    while True:
        # catches wrong inputs
        try:
            sprint_days = int(input("Enter number of sprint days: "))
            if sprint_days <=0:
                print("Invalid input. Please enter an integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer greater than 0.")
    # While there is not a correct input
    while True:
        # catches wrong inputs
        try:
            num_members = int(input("Enter number of team members: "))
            if num_members <=0:
                print("Invalid input. Please enter an integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer greater than 0.")

if __name__ == "__main__":
    calculate_team_capacity() 