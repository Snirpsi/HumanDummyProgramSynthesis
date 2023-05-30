#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A endless loop that removes numbers.
    for number in numbers:
        if number == numbers:
            numbers.remove(number)
    print(numbers)

