#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers. """    
    
    # Create a list with 10 numbers
    numbers = [1,2,3,4,5,6,7,8,9,10]
    
    # Add numbers to the list
    numbers += [-1,-2,-3,-4,-5,-6,-7,-8,-9]
    
    # Print the list
    print(numbers)
    
    # Print the list after adding one more number
    print(numbers + [1])
    
    # Print the list after adding one more number to the list
    print(numbers + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10])
    
    # Print the list after adding one more number to the list and then subtracting one more number
    print(numbers + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10] + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10])
    
    # Print the list after adding one more number to the list and then subtracting one more number and then adding one more number
    print(numbers + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10] + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10] + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10])
    
    # Print the list after adding one more number to the list and then subtracting one more number and then adding one more number and then subtracting one more number
    print(numbers + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10] + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10] + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10] + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10])
    
    # Print the list after adding one more number to the list and then subtracting one more number and then adding one more number and then subtracting one more number and then adding one more number
    print(numbers + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10] + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10] + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10] + [-1,-2,-3,-4,-5,-6,-7,-8,-9,10])
    
    # Print the list after adding one more number to the list and then subtracting one more number and then adding one more number and then subtracting one more number and then adding one more number
    print(numbers + [-1,