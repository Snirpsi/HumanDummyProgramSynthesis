#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates user input or removes numbers. """    
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("You chose to remove numbers")
        
    elif choice == "2":
        print("You chose to enumerate numbers")
        
    else:
        print("Invalid choice")
        
