#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds user input and calculates a list of words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'q':
            break
        
    print('The list of words is:', words)
    
    print('The word "aardvark" occurs {} times.'.format(
        sum(1 for word in words if word == 'aardvark')))
    
    print('The word "abandoned" occurs {} times.'.format(
        sum(1 for word in words if word == 'abandoned')))
    
    print('The word "abandoned" occurs {} times.'.format(
        sum(1 for word in words if word == 'abandoned' and word != 'aardvark')))
    
    print('The word "abandoned" occurs {} times.'.format(
        sum(1 for word in words if word == 'abandoned' and word != 'aardvark' and word != 'abandoned'))