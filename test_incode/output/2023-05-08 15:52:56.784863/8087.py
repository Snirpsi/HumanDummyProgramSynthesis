#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A function that enumerates a list of numbers.
    def enumerate(numbers):
        it = iter(numbers)
        count = 0
        while count < len(numbers):
            yield count, it.__next__()
            count += 1
    
    #A function that prints the numbers in the list.
    def print_numbers(numbers):
        for count, number in numbers:
            print(number, end=', ')
            if count < len(numbers)-1:
                print('')
            else:
                print('')
    
    #A function that prints the numbers in the list with spaces between each number.
    def print_numbers_with_spaces(numbers):
        for count, number in numbers:
            print(number, end=' ', end=' ')
            if count < len(numbers)-1:
                print('')
            else:
                print('')
    
    #A function that prints the numbers in the list with spaces between each number except for the last one.
    def print_numbers_with_spaces_except_last(numbers):
        for count, number in numbers:
            print(number, end=' ', end=' ', end=' ')
            if count < len(numbers)-1:
                print('')
            else:
                print('')
    
    #A function that prints the numbers in the list with spaces between each number except for the last one and prints them in reverse order.
    def print_numbers_with_spaces_except_last_reverse(numbers):
        for count, number in numbers:
            print(number, end=' ', end=' ', end=' ', end=' ')
            if count < len(numbers)-1:
                print('')
            else:
                print('')
    
    #A function that prints the numbers in the list with spaces between each number except for the last one and prints them in reverse order and prints them in reverse order.
    def print_numbers_with_spaces_except_last_reverse_and_print(numbers):
        for count, number in numbers:
            print(number, end=' ', end=' ', end=' ', end=' ', end=' ')
            if count < len(numbers)-1:
                print('')
            else:
                print('')
    
    #A function that prints the numbers in the list with spaces between each number except for the last one and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and prints them in reverse order and print

