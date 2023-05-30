#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits and opens user input. """    
    while True:
        print("Welcome to Fruit Shop!")
        print("Please select an option:")
        print("1. Add Fruit")
        print("2. Remove Fruit")
        print("3. Quit")
        option = input("Enter your choice: ")
        if option == "1":
            print("Adding fruit...")
            fruits = input("Enter fruit name: ")
            fruits.append(fruits)
            print("Fruit added!")
        elif option == "2":
            print("Removing fruit...")
            fruits = input("Enter fruit name: ")
            fruits.remove(fruits)
            print("Fruit removed!")
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again")
