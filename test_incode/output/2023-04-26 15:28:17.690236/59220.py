#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes user input. """    
    while True:
        try:
            answer = input("Are you sure you want to quit? [y/N] ")
            if answer.lower() == "y":
                sys.exit()
            else:
                print("Goodbye")
                break
        except KeyboardInterrupt:
            print("Goodbye")
            break
