#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds a list of numbers. """    
    
    # Create a list with 5 elements
    my_list = [1, 2, 3, 4, 5]
    
    # Add each element of the list to another list
    my_list_2 = my_list + [6, 7]
    
    # Print the list
    print(my_list)
    print(my_list_2)
    
    # Print the sum of each element of the list
    print(sum(my_list))
    print(sum(my_list_2))
    
    # Print the difference between each element of the list
    print(