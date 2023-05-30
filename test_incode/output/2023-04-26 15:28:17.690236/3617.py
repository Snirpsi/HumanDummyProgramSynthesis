#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates user input. """    
    while True:
        choice = input('Choose a number: ')
        if choice == '1':
            print('One')
        elif choice == '2':
            print('Two')
        elif choice == '3':
            print('Three')
        elif choice == '4':
            print('Four')
        elif choice == '5':
            print('Five')
        elif choice == '6':
            print('Six')
        elif choice == '7':
            print('Seven')
        elif choice == '8':
            print('Eight')
        elif choice == '9':
            print('Nine')
        elif choice == '0':
            print('Zero')
        else:
            print('Invalid choice')
