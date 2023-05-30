#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a list of numbers or opens a list of words. """    
    
    words = []
    numbers = []
    
    while True:
        try:
            number = int(input('Enter a number: '))
        except ValueError:
            print('Invalid number')
            continue
        else:
            numbers.append(number)
            
        while True:
            try:
                word = input('Enter a word: ')
            except ValueError:
                print('Invalid word')
                continue
            else:
                words.append(word)
                break
        
        print('The numbers are:', numbers)
        print('The words contain:', words)
        
        print('Would you like to enter another number? [y/n]')
        answer = input()
        
        if answer == 'y':
            continue
        elif answer == 'n':
            break
        else:
            print('Invalid input')
            
    print('Goodbye!')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
