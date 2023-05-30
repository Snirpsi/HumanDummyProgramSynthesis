#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that opens user input.
    while True:
        choice = input("Do you want to play again? y/n: ")
        if choice.lower() == "y":
            break
        else:
            print("Sorry, I didn't understand that.")

