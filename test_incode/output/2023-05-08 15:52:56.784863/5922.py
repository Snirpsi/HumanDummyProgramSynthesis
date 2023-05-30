#!/usr/bin/python3
if __name__ == '__main__':
    #A endless loop that opens user input.
    while True:
        choice = input("\nDo you want to play a game? y/n: ")
        if choice == 'y':
            main()
        elif choice == 'n':
            break
        else:
            print("Invalid input. Please try again.")

