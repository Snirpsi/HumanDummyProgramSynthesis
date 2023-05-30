#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers or adds a list of words. """    
    while True:
        command = input('Enter a command: ')
        if command == 'exit':
            break
        elif command == 'add':
            add(*input('Enter a list of numbers: ').split())
        elif command == 'addword':
            add(*input('Enter a list of words: ').split())
        else:
            print('Invalid command')
            
