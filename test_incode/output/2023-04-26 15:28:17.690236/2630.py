#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates numbers and prints a list of words. """    
    words = []
    
    while True:
        number = int(input('Enter a number: '))
        words.append(str(number))
        
        if number == 0: break
        
    print('The words are:')
    for word in words:
        print(word)
        
    print('Thank you for using my program!')
    
