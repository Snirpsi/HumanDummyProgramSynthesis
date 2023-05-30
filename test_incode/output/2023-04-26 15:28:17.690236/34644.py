#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and multiplyes user input. """    
    
    words_to_remove = input("Enter a list with words to remove: ")
    
    words_to_remove = words_to_remove.split()
    
    words_to_remove.sort()
    
    words_to_remove = " ".join(words_to_remove)
    
    words_to_remove = int(words_to_remove)
    
    words_to_remove = words_to_remove * 