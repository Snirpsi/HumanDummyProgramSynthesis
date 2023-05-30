#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        choice = input("\nEnter your choice: ")
        if choice == "1":
            choice = "A"
        elif choice == "2":
            choice = "B"
        elif choice == "3":
            choice = "C"
        elif choice == "4":
            choice = "D"
        elif choice == "5":
            choice = "E"
        elif choice == "6":
            choice = "F"
        elif choice == "7":
            choice = "G"
        elif choice == "8":
            choice = "H"
        elif choice == "9":
            choice = "I"
        elif choice == "0":
            choice = "J"
        else:
            print("Invalid choice.")
