#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words or adds words. """    
    while True:
        word = input('Enter a word: ')
        word = word.lower()
        word = word.split()
        
        if word == []:
            print('No more words to enter')
            break
        
        print(' '.join(word))
        
        print('Press enter to exit')
        input()
        
    print('Goodbye!')
