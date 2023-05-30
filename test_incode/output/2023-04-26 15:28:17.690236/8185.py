#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or converts a list of numbers. """    
    
    fruits = ['apple', 'orange', 'banana', 'pear', 'grape']
    
    while True:
        fruits.append(input('Enter a fruit: '))
        
        if input('Do you want to convert a list of numbers? (y/n)') == 'y':
            fruits = convert_list_of_numbers(fruits)
        else:
            print('You entered the following fruits:')
            for fruit in fruits:
                print(