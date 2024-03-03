def calculate_average_velocity():
    # While there is not a correct input
    while True:
        # catches wrong inputs
        try:
            print("Enter sprint times separated by space (e.g., 140 150 160):")
            sprint_times = list(map(int, input().split()))
            # if there is no input
            if len(sprint_times) < 1:
                print("Please enter at least one sprint time.")
                continue
            average_velocity = round(sum(sprint_times) / len(sprint_times),1)

            # Display message to user
            print(" ")
            print("Sprint Team's Average Velocity:", average_velocity)
            print(" ")

            break
        except ValueError:
            print("Invalid input. Please enter sprint times as integers separated by spaces.")

if __name__ == "__main__":
    calculate_average_velocity()    