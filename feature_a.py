def calculate_average_velocity():
    print("Enter sprint times separated by space (e.g., 140 150 160):")
    sprint_times = list(map(int, input().split()))
    # if there is no input
    if len(sprint_times) < 1:
        print("Please enter at least one sprint time.")
    else: 
        average_velocity = round(sum(sprint_times) / len(sprint_times),1)
        print(average_velocity)

if __name__ == "__main__":
    calculate_average_velocity()