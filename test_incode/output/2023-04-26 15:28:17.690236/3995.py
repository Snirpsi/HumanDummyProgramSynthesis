#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers or stores a list of words. """    
    
    words = []
    
    while True:
        
        command = input('Enter a command: ')
        
        if command == 'quit':
            break
        
        elif command == 'add':
            
            number = int(input('Enter a number: '))
            words.append(number)
            
        elif command == 'store':
            
            words.append(input('Enter a word: '))
            
        else:
            print('Unknown command')
            
    print('\n'.join(words))
    
