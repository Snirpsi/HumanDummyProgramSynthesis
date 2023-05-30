#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that returns user input.
    while True:
        choice = input("Do you want to play again? [y/n] ")
        if choice == 'y':
            break
        else:
            print("Sorry, I didn't understand that.")

