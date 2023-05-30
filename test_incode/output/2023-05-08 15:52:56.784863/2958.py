#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A function that removes numbers.
    def remove_numbers(numbers):
        numbers = [x for x in numbers if x != 3]
        return numbers
    numbers = remove_numbers(numbers)
    print(numbers)

