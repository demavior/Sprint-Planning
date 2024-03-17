from feature_a import validate_average_velocity
from feature_b import validate_positive_integer

def show_test_result(input, expected_output):
    print("Input:", input,"\n")
    print("Expected Output:")
    print(expected_output)
    print("Actual Output:")

def test_correct_A():
    sprint_times = '140 150 160'
    expected_output = "Sprint Team's Average Velocity: 150.0\nTrue"
    print("Test happy path:")
    show_test_result(sprint_times, expected_output)
    print(validate_average_velocity(sprint_times))
    print("")

def test_empty_A():
    sprint_times = ''
    expected_output = "Please enter at least one sprint time.\nFalse"
    print("Test empty input:")
    show_test_result(sprint_times, expected_output)
    print(validate_average_velocity(sprint_times))
    print("")

def test_invalid_A():
    sprint_times = ['ABCD a xyz', '... -- 23']
    expected_output = "Invalid input. Please enter sprint times as integers separated by spaces.\nFalse"
    print("Test invalid values:")
    for input_value in sprint_times:
        show_test_result(input_value, expected_output)
        print(validate_average_velocity(input_value))
        print("")

def test_negative_A():
    sprint_times = '-140 -150 -160'
    expected_output = "Please enter positive integer values.\nFalse"
    print("Test negative values:")
    show_test_result(sprint_times, expected_output)
    print(validate_average_velocity(sprint_times))
    print("")

def test_correct_B():
    number = 5
    expected_output = 'True'
    print("Test happy path:")
    show_test_result(number, expected_output)
    print(validate_positive_integer(number))
    print("")

def test_empty_B():
    number = ''
    expected_output = 'Invalid input. Please enter an integer value.\nFalse'
    print("Test empty value:")
    show_test_result(number, expected_output)
    print(validate_positive_integer(number))
    print("")

def test_invalid_B():
    number = 'xPd'
    expected_output = 'Invalid input. Please enter an integer value.\nFalse'
    print("Test invalid value:")
    show_test_result(number, expected_output)
    print(validate_positive_integer(number))
    print("")

def test_negative_B():
    number = -8
    expected_output = 'Invalid input. Please enter a positive value.\nFalse'
    print("Test negative value:")
    show_test_result(number, expected_output)
    print(validate_positive_integer(number))
    print("")

if __name__ == '__main__':
    print("TEST FEATURE A:\n")
    test_correct_A()
    test_empty_A()
    test_invalid_A()
    test_negative_A()
    print("TEST FEATURE B:\n")
    test_correct_B()
    test_empty_B()
    test_invalid_B()
    test_negative_B()