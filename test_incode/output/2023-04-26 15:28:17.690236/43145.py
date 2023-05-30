#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits and opens numbers. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        for fruit in fruits:
            print('Opening {}'.format(fruit))
            
            number = input('Enter a number: ')
            
            print('Closing {}'.format(fruit))
            
            number = int(number)
            
            if number < 10:
                print('{} is too small, try again'.format(number))
            elif number > 1000:
                print('{} is too big, try again'.format(number))
            else:
                print('{} is {}'.format(number, fruit))
                
