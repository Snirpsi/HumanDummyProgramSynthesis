#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes fruits. """    
    
    # Read in the fruit list
    fruits = read_from_file('fruits.txt')
    
    # Remove all fruits
    remove_from_list(fruits)
    
    # Write the new fruit list
    write_to_file('fruits.txt', fruits)
    
    # Print the new fruit list
    print('New fruit list:')
    print_list(fruits)
    
