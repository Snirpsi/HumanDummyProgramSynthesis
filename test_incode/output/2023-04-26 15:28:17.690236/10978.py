#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input or removes user input. """    
    while True:
        choice = input('Enter your choice: ')
        if choice == 'exit':
            break
        elif choice == 'add':
            print('You chose to add an item')
        elif choice == 'remove':
            print('You chose to remove an item')
        elif choice == 'clear':
            print('You chose to clear the list')
        elif choice == 'quit':
            print('Goodbye')
        else:
            print('Invalid choice')
    print('Goodbye')
    
