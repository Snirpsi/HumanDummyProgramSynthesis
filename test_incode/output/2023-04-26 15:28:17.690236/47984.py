#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    numbers = range(1,100)
    
    while True:
        for number in numbers:
            print(number)
        
        choice = input('Press enter to continue: ')
        
        if choice == '':
            break
        
        numbers.append(int(choice))
        
    print('Done!')
    
