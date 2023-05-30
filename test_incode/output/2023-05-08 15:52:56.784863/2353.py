#!/usr/bin/python3
if __name__ == '__main__':
    #A function that prints user input.
    def print_user_input():
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("You chose option 1")
        elif choice == "2":
            print("You chose option 2")
        else:
            print("You chose option 3")
            
    print_user_input()

