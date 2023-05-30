#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input. """    
    while True:
        choice = input("Enter your choice: ")
        if choice == 'quit':
            break
        elif choice == '1':
            print('1')
        elif choice == '2':
            print('2')
        elif choice == '3':
            print('3')
        elif choice == '4':
            print('4')
        elif choice == '5':
            print('5')
        elif choice == '6':
            print('6')
        elif choice == '7':
            print('7')
        elif choice == '8':
            print('8')
        elif choice == '9':
            print('9')
        elif choice == '0':
            print('0')
        elif choice == 'q':
            print('Bye!')
            break
        else:
            print('Invalid input')
