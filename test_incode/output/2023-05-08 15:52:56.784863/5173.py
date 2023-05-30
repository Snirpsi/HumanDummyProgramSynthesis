#!/usr/bin/python3
if __name__ == '__main__':
    #A function that prints user input.
    def print_user_input():
        choice = input("Please select an option: ")
        if choice == "1":
            print("You chose option 1")
        elif choice == "2":
            print("You chose option 2")
        elif choice == "3":
            print("You chose option 3")
        else:
            print("Invalid choice")
    print_user_input()

