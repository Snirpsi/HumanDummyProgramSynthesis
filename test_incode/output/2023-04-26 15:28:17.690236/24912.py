#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a list of numbers. """    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Multiply each number in the list by 2
    products = [x * 2 for x in numbers]
    
    # Print the product
    print('The product of the numbers is', products)
    
    # Print the product of the numbers in reverse order
    print('The product of the numbers in reverse order is', products[::-1])
    
    # Print the product of the numbers in reverse order using list comprehension
    print('The product of the numbers in reverse order using list comprehension is', 
          [x * 2 for x in numbers[::-1]])
    
    # Print the product of the numbers in reverse order using map and lambda
    print('The product of the numbers in reverse order using map and lambda is', 
          list(map(lambda x: x * 2, numbers[::-1])))
    
    # Print the product of the numbers in reverse order using map and lambda and 
    # unpacking
    print('The product of the numbers in reverse order using map and lambda and unpacking is', 
          list(map(lambda x, y: x * y, numbers[::-1])))
    
    # Print the product of the numbers in reverse order using map and lambda and 
    # unpacking and unpacking
    print('The product of the numbers in reverse order using map and lambda and unpacking and unpacking is', 
          list(map(lambda x, y: x * y, numbers[::-1], numbers[::-1])))
    
    # Print the product of the numbers in reverse order using map and lambda and unpacking and unpacking and unpacking
    print('The product of the numbers in reverse order using map and lambda and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and unpacking and 