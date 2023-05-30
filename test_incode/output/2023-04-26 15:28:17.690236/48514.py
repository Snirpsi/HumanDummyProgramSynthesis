#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of words or opens user input. """    
    
    words = []
    
    while True:
        
        command = input('> ')
        
        if command == 'exit':
            break
        
        elif command == 'add':
            words.append(input('> '))
        
        elif command == 'remove':
            words.pop(int(input('> ')))
        
        else:
            print('Unknown command')
        
    print('\n'.join(words))
    
    
