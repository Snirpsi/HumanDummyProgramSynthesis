#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that enumerates a list of numbers.
    def enumerate(numbers):
        for index, number in enumerate(numbers):
            yield index, number

    #A function that prints the numbers in an enumerated list.
    def print_numbers(numbers):
        for index, number in enumerate(numbers):
            print(number, end=', ')
        print('')

    #A function that prints the numbers in an enumerated list using an f-string.
    def print_numbers_with_f(numbers):
        for index, number in enumerate(numbers):
            print(f'{number:>5}', end=', ')
        print('')

    #A function that prints the numbers in an enumerated list using an f-string and an argument to specify the starting index.
    def print_numbers_with_f2(numbers, start):
        for index, number in enumerate(numbers):
            print(f'{number:>{start}}', end=', ')
        print('')

    #A function that prints the numbers in an enumerated list using an f-string and an argument to specify the starting index and a separator character.
    def print_numbers_with_f3(numbers, start, separator):
        for index, number in enumerate(numbers):
            print(f'{number:>{start}{separator}}', end=', ')
        print('')

    #A function that prints the numbers in an enumerated list using an f-string and an argument to specify the starting index and a separator character and an argument to specify the ending index.
    def print_numbers_with_f4(numbers, start, separator, ending):
        for index, number in enumerate(numbers):
            print(f'{number:>{start}{separator}{ending}}', end=', ')
        print('')

    #A function that prints the numbers in an enumerated list using an f-string and an argument to specify the starting index and a separator character and an argument to specify the ending index and a separator character.
    def print_numbers_with_f5(numbers, start, separator, ending, separator2):
        for index, number in enumerate(numbers):
            print(f'{number:>{start}{separator}{ending}{separator2}}', end=', ')
        print('')

    #A function that prints the numbers in an enumerated list using an f-string and an argument to specify the starting index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator character and an argument to specify the ending index and a separator 

