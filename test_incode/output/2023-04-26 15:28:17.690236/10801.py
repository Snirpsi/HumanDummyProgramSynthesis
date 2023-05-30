#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds numbers and stores words. """    
    
    words = []
    
    while True:
        number = int(input('Enter a number: '))
        
        if number < 0 or number > 1000:
            print('Invalid number')
            continue
        
        if number % 2 == 0:
            words.append(str(number))
        else:
            words.append('X')
        
        print(' '.join(words))
        
        print('Do you want to add another number? Y/N')
        
        choice = input('> ')
        
        if choice == 'Y' or choice == 'y':
            continue
        
        elif choice == 'N' or choice == 'n':
            break
        
        else:
            print('Invalid input')
            
    print('Goodbye!')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
