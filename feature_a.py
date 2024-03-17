def validate_average_velocity(user_input):
    # Catches wrong inputs
    try:
        sprint_times = list(map(int, user_input.split()))
        # Verify input
        if len(sprint_times) < 1:
            print("Please enter at least one sprint time.")
            return (False)
        average_velocity = round(sum(sprint_times) / len(sprint_times),1)
        # Verify positive
        if average_velocity < 0:
            print("Please enter positive integer values.")
            return (False)

        # Display message to user
        print("Sprint Team's Average Velocity:", average_velocity)

        return (True)
    except ValueError:
        print("Invalid input. Please enter sprint times as integers separated by spaces.")
        return(False)
def calculate_average_velocity():
    # While input is not valid
    while not validate_average_velocity(input("Enter sprint times separated by space (e.g., 140 150 160): ")):
        pass
    print(" ")

if __name__ == "__main__":
    calculate_average_velocity()