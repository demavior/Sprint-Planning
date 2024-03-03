def display_menu():
    print("What do you want to calculate?")
    print("1. Sprint team's average velocity")
    print("2. Team Effort-Hour Capacity")
    print("3. Exit")

def main():
    display_menu()
    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            print("calculate_average_velocity")
            #calculate_average_velocity()
            return
        elif choice == '2':
            print("calculate_team_capacity")
            #calculate_team_capacity()
            return
        elif choice == '3':
            return
        else:
            print("Invalid choice. Please enter either 1, 2 or 3.")

if __name__ == "__main__":
    main()