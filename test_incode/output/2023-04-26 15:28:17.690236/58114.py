#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a list of words or iterates over numbers. """    
    
    words = []
    
    while True:
        number = int(input('Enter a number: '))
        
        if number == 0: break
        
        words.append(number)
        
    print('The words are: ')
    
    for word in words:
        print(word)
        
    print('The numbers are: ')
    
    for number in words:
        print(number)
        
    print('The sum of the numbers is {}.'.format(sum(words)))
    
    print('The sum of the words is {}.'.format(sum(