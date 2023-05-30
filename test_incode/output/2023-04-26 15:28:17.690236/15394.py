#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of numbers. """    
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        
        numbers.remove(numbers.pop())
        
        print('Removed ' + str(len(numbers)) + ' numbers')
        
        if numbers == []:
            break
        
        print('Press enter to exit')
        
        raw_input()
        
    print('Done')
    
