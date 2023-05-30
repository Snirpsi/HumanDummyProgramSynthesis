#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates a list of numbers or calculates numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    for index, number in enumerate(numbers):
        print("{}. {}".format(index + 1, number))
    
    print("\nCalculating numbers...")
    
    numbers_calculated = [sum(numbers), sum(numbers), sum(numbers)]
    
    print("\nResult:")
    
    print("Sum of numbers: {}".format(numbers_calculated[0]))
    print("Sum of numbers: {}".format(numbers_calculated[1]))
    print("Sum of numbers: {}".format(numbers_calculated[2]))
    
    print("\nResult:")
    
    print("Sum of numbers: {}".format(numbers_calculated[0] + numbers_calculated[1] + numbers_calculated[2]))
    
    print("\nResult:")
    
    print("Sum of numbers: {}".format(numbers_calculated[0] + numbers_calculated[1] + numbers_calculated[2] + numbers_calculated[3]))
    
    print("\nResult:")
    
    print("Sum of numbers: {}".format(numbers_calculated[0] + numbers_calculated[1] + numbers_calculated[2] + numbers_calculated[3] + numbers_calculated[4]))
    
    print("\nResult:")
    
    print("Sum of numbers: {}".format(numbers_calculated[0] + numbers_calculated[1] + numbers_calculated[2] + numbers_calculated[3] + numbers_calculated[4] + numbers_calculated[5]))
    
    print("\nResult:")
    
    print("Sum of numbers: {}".format(numbers_calculated[0] + numbers_calculated[1] + numbers_calculated[2] + numbers_calculated[3] + numbers_calculated[4] + numbers_calculated[5] + numbers_calculated[6]))
    
    print("\nResult:")
    
    print("Sum of numbers: {}".format(numbers_calculated[0] + numbers_calculated[1] + numbers_calculated[2] + numbers_calculated[3] + numbers_calculated[4] + numbers_calculated[5] + numbers_calculated[6] + numbers_calculated[7]))
    
    print("\nResult:")
    
    print("Sum of numbers: {}".format(numbers_calculated[0] + numbers_calculated[1] + numbers_calculated[2] + numbers_calculated[3] + numbers_calculated[4] + numbers_calculated[5] + numbers_calculated[6] + numbers_calculated[7] + numbers_calculated[8]))
    
    print("\nResult:")
    
    print("Sum of numbers: {}".format(numbers_calculated[0] + numbers_calculated[1] + numbers_calculated[2] + numbers_calculated[3] + numbers_calculated[4] + numbers_calculated[5