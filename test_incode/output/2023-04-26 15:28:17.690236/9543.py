#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers and adds a list of words. """    
    numbers = [1,2,3,4,5,6,7,8,9,10]
    words = ['one','two','three','four','five','six','seven','eight','nine','ten']
    
    while True:
        number = int(input('Enter a number: '))
        word = str(input('Enter a word: '))
        
        if number > 10:
            print('Sorry, you cannot enter more than 10 numbers. Please try again.')
            continue
        
        if number < 1:
            print('Sorry, you cannot enter a number less than 1. Please try again.')
            continue
        
        if word not in words:
            print('Sorry, that word is not in the list. Please try again.')
            continue
        
        numbers.append(number)
        
        print('The number %d is %d and it is in the list %s' % (number, number