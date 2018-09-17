def minmax(*arguments):

    for i in arguments:
        if not isinstance(i, int) and not isinstance(i, float):
            print("Please enter numbers!")
            quit()

    smallest_number = arguments[0]
    largest_number = arguments[0]
    for i in arguments[1: ]:
        if i < smallest_number:
            smallest_number = i
        if i > largest_number:
            largest_number = i
    return smallest_number,largest_number

print(minmax(5.7,8,6,-21,-13,13.5))