#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of words or enumerates a list of numbers. """    
    
    words = ['hello', 'world', '!']
    numbers = [1, 2, 3, 4, 5]
    
    numbers_multiply = multiply(numbers, words)
    
    print(numbers_multiply)
    
    numbers_enumerate = enumerate(numbers)
    
    print(numbers_enumerate)
    
    numbers_multiply_by_two = multiply(numbers, 2)
    
    print(numbers_multiply_by_two)
    
    numbers_multiply_by_two_by_two = multiply(numbers, 2, 2)
    
    print(numbers_multiply_by_two_by_two)
    
    numbers_multiply_by_two_by_three = multiply(numbers, 2, 3)
    
    print(numbers_multiply_by_two_by_three)
    
    numbers_multiply_by_two_by_three_by_three = multiply(numbers, 2, 3, 3)
    
    print(numbers_multiply_by_two_by_three_by_three)
    
    numbers_multiply_by_two_by_three_by_four = multiply(numbers, 2, 3, 4, 5)
    
    print(numbers_multiply_by_two_by_three_by_four)
    
    numbers_multiply_by_two_by_three_by_four_by_five = multiply(numbers, 2, 3, 4, 5, 5)
    
    print(numbers_multiply_by_two_by_three_by_four_by_five)
    
    numbers_multiply_by_two_by_three_by_four_by_five_by_six = multiply(numbers, 2, 3, 4, 5, 5, 6)
    
    print(numbers_multiply_by_two_by_three_by_four_by_five_by_six)
    
    numbers_multiply_by_two_by_three_by_four_by_five_by_six_by_seven = multiply(numbers, 2, 3, 4, 5, 5, 6, 7)
    
    print(numbers_multiply_by_two_by_three_by_four_by_five_by_six_by_seven)
    
    numbers_multiply_by_two_by_three_by_four_by_five_by_six_by_seven_by_eight = multiply(numbers, 2, 3, 4, 5, 5, 6, 7, 8)
    
    print(numbers_multiply_by_two_by_three_by_four_by_five_by_six_by_seven_by_eight)
    
    numbers_multiply_by_two_by_three_by_four_by_five_by_six_by_seven_by_eight_by_nine = multiply(numbers, 2, 3, 4, 5, 5, 6, 7, 8, 9)
    
    print(numbers_multiply_by_two_by_three_by_four_by_five_by_six_by_seven_by_eight_by_nine)
    
    numbers_multiply_by_