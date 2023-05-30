#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints user input or enumerates user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        choice = sys.argv[1]
    else:
        choice = 'a'
    
    if choice == 'a':
        print('Enter a number:')
        number = input()
        print('You entered', number)
    elif choice == 'b':
        print('Enter a string:')
        string = input()
        print('You entered', string)
    elif choice == 'c':
        print('Enter a boolean:')
        boolean = input()
        print('You entered', boolean)
    elif choice == 'd':
        print('Enter a list:')
        list = input()
        print('You entered', list)
    elif choice == 'e':
        print('Enter a tuple:')
        tuple = input()
        print('You entered', tuple)
    elif choice == 'f':
        print('Enter a dictionary:')
        dictionary = input()
        print('You entered', dictionary)
    elif choice == 'g':
        print('Enter a set:')
        set = input()
        print('You entered', set)
    elif choice == 'h':
        print('Enter a set-like object:')
        setlike = input()
        print('You entered', setlike)
    elif choice == 'i':
        print('Enter a frozenset:')
        frozenset = input()
        print('You entered', frozenset)
    elif choice == 'j':
        print('Enter a frozenset-like object:')
        frozensetlike = input()
        print('You entered', frozensetlike)
    elif choice == 'k':
        print('Enter a set-like object:')
        setlike = input()
        print('You entered', setlike)
    elif choice == 'l':
        print('Enter a set-like object:')
        setlike = input()
        print('You entered', setlike)
    elif choice == 'm':
        print('Enter a set-like object:')
        setlike = input()
        print('You entered', setlike)
    elif choice == 'n':
        print('Enter a set-like object:')
        setlike = input()
        print('You entered', setlike)
    elif choice == 'o':
        print('Enter a set-like object:')
        setlike = input()
        print('You entered', setlike)
    elif choice == 'p':
        print('Enter a set-like object:')
        setlike = input()
        print('You entered', setlike)
    elif choice == 'q':
        print('Enter a set-like object:')
        setlike = input()
        print('You entered', setlike)
    elif choice == 'r':
        print('Enter a set-like object:')
        setlike = input()
        print('You entered', setlike)
    elif choice == 's':
        print('Enter a set-like 