#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that removes a list of numbers.
    def remove_numbers(numbers):
        numbers_copy = numbers.copy()
        for number in numbers_copy:
            if number in numbers_copy:
                numbers_copy.remove(number)
        return numbers_copy
    print(remove_numbers(numbers))

