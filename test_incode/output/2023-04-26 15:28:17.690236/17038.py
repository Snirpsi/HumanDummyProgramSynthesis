#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes user input or returns a list of words. """    
    
    # Get the user input from the user
    wordlist = input('Enter a word: ')
    
    # If the user input is a list, return it
    if wordlist:
        print('The words are: ', wordlist)
    else:
        print('The words are: ', wordlist.split())
    
    # If the user input is not a list, return it as a string
    else:
        print('The words are: ', wordlist.