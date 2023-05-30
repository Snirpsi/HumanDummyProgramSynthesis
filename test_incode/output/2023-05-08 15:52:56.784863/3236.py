#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that removes a list of numbers.
    def remove_numbers(numbers):
        return list(filter(lambda x: x not in numbers, numbers))
    print(remove_numbers(numbers))

