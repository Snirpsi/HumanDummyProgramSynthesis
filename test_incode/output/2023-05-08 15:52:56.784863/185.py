#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that removes user input.
    while True:
        choice = input("Do you want to continue? y/n: ")
        if choice == 'y':
            break
        else:
            print("Goodbye")

