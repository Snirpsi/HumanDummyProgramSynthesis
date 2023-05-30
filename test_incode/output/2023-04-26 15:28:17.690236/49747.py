#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or removes a list of words. """    
    while True:
        word = input("Enter a word: ")
        if word == "quit":
            break
        elif word == "fruit":
            fruit = input("Enter a fruit: ")
            if fruit == "apple":
                print("You chose apple!")
            elif fruit == "banana":
                print("You chose banana!")
            elif fruit == "cherry":
                print("You chose cherry!")
            elif fruit == "grape":
                print("You chose grape!")
            elif fruit == "orange":
                print("You chose orange!")
            elif fruit == "pineapple":
                print("You chose pineapple!")
            elif fruit == "strawberry":
                print("You chose strawberry!")
            elif fruit == "watermelon":
                print("You chose watermelon!")
            elif fruit == "yellow":
                print("You chose yellow!")
            elif fruit == "white":
                print("You chose white!")
            else:
                print("Invalid fruit.")
        elif word == "remove":
            remove = input("Enter a word: ")
            if remove == "apple":
                print("You chose apple!")
            elif remove == "banana":
                print("You chose banana!")
            elif remove == "cherry":
                print("You chose cherry!")
            elif remove == "grape":
                print("You chose grape!")
            elif remove == "orange":
                print("You chose orange!")
            elif remove == "pineapple":
                print("You chose pineapple!")
            elif remove == "strawberry":
                print("You chose strawberry!")
            elif remove == "watermelon":
                print("You chose watermelon!")
            elif remove == "yellow":
                print("You chose yellow!")
            elif remove == "white":
                print("You chose white!")
            else:
                print("Invalid fruit.")
        else:
            print("Invalid word.")
