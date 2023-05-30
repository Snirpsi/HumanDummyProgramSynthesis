#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of numbers or adds a list of words. """    
    while True:
        number = int(input('Enter a number: '))
        word = str(input('Enter a word: '))
        
        if number == 0 or number == -1:
            print('Invalid input')
            continue
        
        if word == '':
            print('Invalid input')
            continue
        
        if word == 'quit':
            break
        
        if number % 2 == 0:
            print('The number {} is even'.format(number))
        else:
            print('The number {} is odd'.format(number))
        
        print('The word {} multiplied by the number {} is {}'.format(word, number, number*word))
        
        print('Press enter to exit')
        
        input()
        
    print('Goodbye')
