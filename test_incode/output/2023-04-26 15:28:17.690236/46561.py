#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over fruits or adds user input. """    
    fruit = input("Enter a fruit: ")
    
    fruit = fruit.lower()
    
    if fruit == "apple":
        print("Oh no! You can't eat apples.")
    elif fruit == "banana":
        print("Oh no! You can't eat bananas.")
    elif fruit == "orange":
        print("Oh no! You can't eat oranges.")
    elif fruit == "mango":
        print("Oh no! You can't eat mangos.")
    else:
        print("Oh no! You can't eat anything else.")
    
