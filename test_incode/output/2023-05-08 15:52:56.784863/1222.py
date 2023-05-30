#!/usr/bin/python3
if __name__ == '__main__':
    #A function that prints user input.
    def print_user_input():
        choice = input("Please choose a number from 1 to 10: ")
        if choice == '1':
            print("You chose number 1")
        elif choice == '2':
            print("You chose number 2")
        elif choice == '3':
            print("You chose number 3")
        elif choice == '4':
            print("You chose number 4")
        elif choice == '5':
            print("You chose number 5")
        elif choice == '6':
            print("You chose number 6")
        elif choice == '7':
            print("You chose number 7")
        elif choice == '8':
            print("You chose number 8")
        elif choice == '9':
            print("You chose number 9")
        else:
            print("Invalid choice.")
    print_user_input()

