#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input. """    
    while True:
        choice = input('Choose a number from 1-10: ')
        if choice == 'quit':
            break
        elif choice == '1':
            print('The number chosen is 1.')
        elif choice == '2':
            print('The number chosen is 2.')
        elif choice == '3':
            print('The number chosen is 3.')
        elif choice == '4':
            print('The number chosen is 4.')
        elif choice == '5':
            print('The number chosen is 5.')
        elif choice == '6':
            print('The number chosen is 6.')
        elif choice == '7':
            print('The number chosen is 7.')
        elif choice == '8':
            print('The number chosen is 8.')
        elif choice == '9':
            print('The number chosen is 9.')
        elif choice == '10':
            print('The number chosen is 10.')
        else:
            print('Invalid choice.')
            
