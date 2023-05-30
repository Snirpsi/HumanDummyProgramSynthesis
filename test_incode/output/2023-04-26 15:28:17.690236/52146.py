#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words. """    
    while True:
        print("Enter a word:")
        word = input()
        if word == 'quit':
            break
        else:
            print(word)
