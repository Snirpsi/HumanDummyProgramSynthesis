#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words or calculates words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        if word == 'help':
            print('''
            Enter a word: 
            quit
            ''')
        
        if word not in words:
            words.append(word)
        
    print('\n'.join(words))
    
