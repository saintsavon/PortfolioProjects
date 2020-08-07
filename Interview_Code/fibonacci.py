def fibonacci(starting_number, sequence_length=10):  # Argument error resolved
    """
    Fibonacci sequence calculator
    :param starting_number:
    :param sequence_length:
    :return Fibonacci sequence:
    """
    if starting_number == 0:
        a, b = 0, 1
    elif starting_number == 1:
        a, b = 1, 1
    else:
        print("Please enter a 0 or 1!")  # Error resolved
        return  # Formatting error resolved

    sequence = starting_number
    for i in range(sequence_length - 1):
        sequence = str(sequence) + " {}".format(str(b))  # Error resolved
        a, b = b, a + b
    print(sequence)  # Error resolved


# DO NOT ADJUST THE TEST PARAMETERS BELOW
# THE CONSOLE OUTPUT SHOULD MATCH THIS:
#     Please enter a 0 or 1!
#     0 1 1 2 3
#     1 1 2 3 5
#     1 1 2 3 5 8 13 21 34 55
fibonacci(2, 5)
fibonacci(0, 5)
fibonacci(1, 5)
fibonacci(1)
