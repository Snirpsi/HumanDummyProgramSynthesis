#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words or opens user input. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'exit':
            break
        
        if word == '':
            continue
        
        words.append(word)
    
    print('\n'.join(words))
    
    
