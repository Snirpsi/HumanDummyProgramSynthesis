#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that removes a list of numbers.
    def remove_numbers(numbers):
        numbers_removed = []
        for number in numbers:
            if number not in numbers_removed:
                numbers_removed.append(number)
        return numbers_removed
    print(remove_numbers(numbers))

