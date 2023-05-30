#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or enumerates user input. """    
    while True:
        answer = input("Enter your answer: ")
        if answer == "exit":
            break
        elif answer == "quit":
            break
        else:
            print(answer)
