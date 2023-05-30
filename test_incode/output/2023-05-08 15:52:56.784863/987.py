#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that removes a list of numbers.
    def remove(numbers):
        numbers = list(filter(lambda x: x not in numbers, numbers))
        return numbers
    print(remove(numbers))

