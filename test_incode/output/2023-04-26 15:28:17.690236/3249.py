#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        choice = input("Do you want to convert a number? [y/n]")
        if choice == 'y':
            number = input("Enter a number: ")
            number = int(number)
            answer = int(number * 2)
            print(answer)
        elif choice == 'n':
            break
        else:
            print("Invalid input. Please try again.")
