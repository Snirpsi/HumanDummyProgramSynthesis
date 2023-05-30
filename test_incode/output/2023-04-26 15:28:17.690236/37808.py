#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words or returns a port. """    
    
    while True:
        word = input("Enter a word: ")
        if word == 'exit':
            break
        elif word == 'help':
            print("\nAvailable commands:")
            print("\texit: exits the program")
            print("\thelp: prints this help")
            print("\tword: prints a word or prints a port")
        else:
            print(word)
            
