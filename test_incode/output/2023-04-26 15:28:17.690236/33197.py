#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits. """    
    fruits = ['apple', 'banana', 'cherry']
    while True:
        print('Fruits:')
        for fruit in fruits:
            print('\t' + fruit)
        choice = input('Enter a choice: ')
        if choice == 'quit':
            break
        else:
            fruits.remove(choice)
    print('Done.')

<|/ file source=github ext=.py |>