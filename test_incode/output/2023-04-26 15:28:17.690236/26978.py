#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input. """    
    while True:
        answer = input("Please enter your answer: ")
        if answer == "quit":
            break
        else:
            print(answer)
            
