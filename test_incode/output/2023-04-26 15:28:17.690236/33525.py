#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers and removes fruits. """    
    
    # Read in numbers and remove fruits.
    numbers = map(int, input().split())
    fruits = map(str, input().split())
    
    # Convert numbers to strings and remove fruits.
    numbers = map(str, numbers)
    fruits = list(fruits)
    
    # Remove fruits.
    numbers = filter(lambda num: num not in fruits, numbers)
    
    # Print the result.
    print(" ".join(numbers))
    
    # 