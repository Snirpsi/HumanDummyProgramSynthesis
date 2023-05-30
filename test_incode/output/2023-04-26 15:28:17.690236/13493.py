#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or multiplyes user input. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        
        multiplier = 1
        
        if word == 'multiply':
            multiplier = int(input('Enter a number: '))
        
        print('The word "' + word + '" multiplied by ' + str(multiplier) + ' is "' + word * multiplier + '".')
        
        print('Do you want to enter another word? (y/n) ')
        
        ans = input('(y/n) ')
        
        if ans == 'y' or ans == 'Y':
            continue
        
        elif ans == 'n' or ans == 'N':
            break
        
        else:
            print('Invalid input. Try again.')
            
    print('Goodbye!')
    
