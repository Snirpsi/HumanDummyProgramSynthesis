#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or multiplyes user input. """    
    while True:
        print("\nPlease select an option:")
        print("1. Print all ports")
        print("2. Multiply user input")
        choice = input("\nEnter your choice: ")
        if choice == "1":
            print("Printing all ports:")
            print_all_ports()
        elif choice == "2":
            print("Multiplying user input:")
            multiply(int(input("Enter your input: ")))
        else:
            print("Invalid choice")
