#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words or adds a list of numbers. """    
    words = ['hello', 'world', 'python', 'is', 'a', 'good', 'day']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    while True:
        print('Type "quit" to quit.')
        print('Type "add" to add numbers')
        print('Type "list" to print list of numbers')
        print('Type "help" to see help')
        command = input('> ')
        if command == 'quit':
            print('Goodbye!')
            break
        elif command == 'add':
            number = int(input('> '))
            words.append(number)
        elif command == 'list':
            print(words)
        elif command == 'help':
            print('Type "add" to add numbers')
            print('Type "list" to print list of numbers')
            print('Type "help" to see help')
        else:
            print('Unknown command')
