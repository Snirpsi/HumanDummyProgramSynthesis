#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates numbers or adds a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while True:
        number = input("Enter a number: ")
        if number == 'done':
            break
        else:
            numbers.append(int(number))
    print("Numbers: ", numbers)
    print("Sum: ", sum(numbers))
    print("Average: ", sum(numbers) / len(numbers))
    print("Standard Deviation: ", 