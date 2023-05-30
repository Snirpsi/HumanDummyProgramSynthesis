#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or converts numbers. """    
    while True:
        word = input('Enter a word: ')
        number = input('Enter a number: ')
        
        if word == 'exit':
            break
        elif word.isdigit():
            number = int(number)
        else:
            number = word
            
        print('The word is', word, 'and the number is', number)
        
        print('Do you want to continue? (y/n)')
        
        answer = input('> ')
        
        if answer.lower() == 'y':
            print('Goodbye!')
            break
        else:
            print('Goodbye!')
            break
            
