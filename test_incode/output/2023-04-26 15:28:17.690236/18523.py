#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or calculates a list of numbers. """    
    while True:
        word = input('Enter a word: ')
        if word == 'quit':
            break
        else:
            number = int(input('Enter a number: '))
            print(word + ' is ' + str(number))
            
    print('Goodbye!')
    
