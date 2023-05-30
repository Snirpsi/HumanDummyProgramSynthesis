#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits or removes words. """    
    while True:
        fruit = input("Enter a fruit or remove a word: ")
        if fruit == "fruit":
            fruit = input("Enter a fruit or remove a word: ")
            if fruit == "fruit":
                print("You won the game!")
                break
            else:
                print("You lost the game!")
                break
        elif fruit == "remove":
            fruit = input("Enter a fruit or remove a word: ")
            if fruit == "fruit":
                print("You won the game!")
                break
            else:
                print("You lost the game!")
                break
        else:
            print("Invalid input")
