#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of numbers and returns words. """    
    words = []
    
    while True:
        number = int(input('Enter a number: '))
        words.append(str(number))
        
        if number == 999:
            break
        
    print('The numbers are: ')
    for number in words:
        print(number)
        
    print('Thank you for using my program!')
    
