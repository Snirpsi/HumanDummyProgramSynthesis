#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over a list of numbers. """    
    
    # Create a list with 10 random numbers
    numbers = [random.randint(1, 10) for _ in range(10)]
    
    # Print the list with 10 random numbers
    print(numbers)
    
    # Print the list with 10 random numbers sorted in ascending order
    print(sorted(numbers, reverse=True))
    
    # Print the list with 10 random numbers sorted in descending order
    print(sorted(numbers, reverse=False))
    
    # Print the list with 10 random numbers sorted in ascending order and in descending order
    print(sorted(numbers, reverse=True, key=lambda x: -x))
    
    # Print the list with 10 random numbers sorted in ascending order and in descending order and in ascending order
    print(sorted(numbers, reverse=True, key=lambda x: -x, key=lambda x: x))
    
    # Print the list with 10 random numbers sorted in ascending order and in descending order and in ascending order and in descending order
    print(sorted(numbers, reverse=True, key=lambda x: -x, key=lambda x: x, key=lambda x: -x))
    
    # Print the list with 10 random numbers sorted in ascending order and in descending order and in ascending order and in descending order and in ascending order and in descending order
    print(sorted(numbers, reverse=True, key=lambda x: -x, key=lambda x: x, key=lambda x: -x, key=lambda x: x))
    
    # Print the list with 10 random numbers sorted in ascending order and in descending order and in ascending order and in descending order and in ascending order and in descending order and in ascending order and in descending order
    print(sorted(numbers, reverse=True, key=lambda x: -x, key=lambda x: x, key=lambda x: -x, key=lambda x: x, key=lambda x: -x, key=lambda x: x, key=lambda x: x))
    
    # Print the list with 10 random numbers sorted in ascending order and in descending order and in ascending order and in descending order and in ascending order and in descending order and in ascending order and in descending order and in ascending order and in descending order
    print(sorted(numbers, reverse=True, key=lambda x: -x, key=lambda x: x, key=lambda x: -x, key=lambda x: x, key=lambda x: -x, key=lambda x: x, key=lambda x: -x, key=lambda x: x, key=lambda x: x, key=lambda x: x, key=lambda x: x))
    
    # Print the list with 10 random numbers sorted in ascending order and in descending order and in ascending order and in descending order and in ascending order and in descending order and in ascending order and in descending order and in ascending order and in descending order 