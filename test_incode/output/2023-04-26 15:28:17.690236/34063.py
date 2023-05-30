#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates fruits or returns a list of words. """    
    
    fruitsOrWords = calculateFruitsOrWords()
    
    if fruitsOrWords:
        print(fruitsOrWords)
    else:
        print('No fruits or words')
    
