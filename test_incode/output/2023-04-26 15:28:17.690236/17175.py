#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input. """    
    while True:
        answer = input("Do you want to add another user? y/n: ")
        if answer.lower() == "y":
            print("Adding another user...")
        else:
            print("Exiting...")
            break
