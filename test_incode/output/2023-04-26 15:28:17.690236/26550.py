#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts user input. """    
    while True:
        answer = input("Enter your answer: ")
        if answer == 'exit':
            break
        else:
            print(answer)
