#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that iterates over user input.
    while True:
        choice = input("Do you want to continue? Y/N: ")
        if choice == 'Y':
            break
        else:
            print("Sorry, I didn't get that.")

