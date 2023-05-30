#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        choice = input("\nEnter your choice: ").lower()
        if choice == 'quit':
            break
        elif choice == '1':
            answer = 1
        elif choice == '2':
            answer = 2
        elif choice == '3':
            answer = 3
        elif choice == '4':
            answer = 4
        elif choice == '5':
            answer = 5
        elif choice == '6':
            answer = 6
        elif choice == '7':
            answer = 7
        elif choice == '8':
            answer = 8
        elif choice == '9':
            answer = 9
        elif choice == '0':
            answer = 0
        else:
            print("Invalid input. Try again.")
