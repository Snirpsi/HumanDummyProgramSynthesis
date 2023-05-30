#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and prints numbers. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
        
        print('The word "{}" appears {} times.'.format(word, len(words)))
        
    print('Thank you for using 