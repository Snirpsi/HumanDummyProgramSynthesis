#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that iterates over user input.
    while True:
        choice = input("Do you want to play a game? [y/n]")
        if choice == 'y':
            play_game()
        elif choice == 'n':
            break
        else:
            print("Invalid input. Try again.")

