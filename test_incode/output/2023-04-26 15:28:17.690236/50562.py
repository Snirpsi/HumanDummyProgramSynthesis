#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns user input. """    
    while True:
        answer = input("Enter your answer: ")
        if answer == "exit":
            break
        else:
            print(answer)
