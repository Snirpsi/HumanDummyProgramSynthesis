#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints fruits or returns a list of words. """    
    
    fruitsOrWords = printFruitsOrWords()
    
    if fruitsOrWords:
        print(fruitsOrWords)
    else:
        print("No fruits or words found.")
    
