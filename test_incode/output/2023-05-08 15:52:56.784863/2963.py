#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that adds user input.
    while True:
        answer = input("Do you want to continue? Y/N: ")
        if answer.lower() == "y":
            break
        else:
            print("Sorry, I didn't understand that.")

