#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates user input or prints words. """    
    while True:
        answer = input("Enter your answer: ")
        if answer == "quit":
            break
        else:
            print(answer)
