#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        answer = input("Do you want to continue? [Y/n] ")
        if answer.upper() == 'Y':
            break
        else:
            print("Exiting...")
            exit()
