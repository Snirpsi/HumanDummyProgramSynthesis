#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input or prints fruits. """    
    while True:
        print("Welcome to my Fruit Shop!")
        print("What would you like to do?")
        print("1. Add an apple")
        print("2. Add an orange")
        print("3. Add an banana")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You chose to add an apple")
            apple = input("What is the name of the apple? ")
            print("The apple is", apple)
        elif choice == "2":
            print("You chose to add an orange")
            orange = input("What is the name of the orange? ")
            print("The orange is", orange)
        elif choice == "3":
            print("You chose to add an banana")
            banana = input("What is the name of the banana? ")
            print("The banana is", banana)
        elif choice == "4":
            print("Thank you for using this program!")
            break
        else:
            print("Invalid choice, please try again.")
