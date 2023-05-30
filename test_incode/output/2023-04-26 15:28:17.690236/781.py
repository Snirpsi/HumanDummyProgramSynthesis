#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens user input. """    
    while True:
        choice = input("Do you want to play a game? [y/n]")
        if choice == "y":
            print("Welcome to my game!")
            play_game()
        elif choice == "n":
            print("Goodbye!")
            quit()
        else:
            print("Invalid input. Try again.")
            
