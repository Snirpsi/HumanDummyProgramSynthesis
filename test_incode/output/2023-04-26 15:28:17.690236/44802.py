#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and enumerates user input. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        words.append(word)
    
    print('\n'.join(words))
    
    print('You entered', len(words), 'words')
    
    print('The words are', ', '.join(words))
    
    print('The first word is', words[0])
    
    print('The last word is', words[-1])
    
    print('The first 5 words are', words[:5])
    
    print('The last 5 words are', words[-5:])
    
    print('The first 10 words are', words[:10])
    
    print('The last 10 words are', words[-10:])
    
    print('The first 100 words are', words[:100])
    
    print('The last 100 words are', words[-100:])
    
    print('The first 1000 words are', words[:1000])
    
    print('The last 1000 words are', words[-1000:])
    
    print('The first 10000 words are', words[:10000])
    
    print('The last 10000 words are', words[-10000:])
    
    print('The first 100000 words are', words[:100000])
    
    print('The last 100000 words are', words[-100000:])
    
    print('The first 1000000 words are', words[:1000000])
    
    print('The last 1000000 words are', words[-1000000:])
    
    print('The first 10000000 words are', words[:10000000])
    
    print('The last 10000000 words are', words[-10000000:])
    
    print('The first 100000000 words are', words[:100000000])
    
    print('The last 100000000 words are', words[-100000000:])
    
    print('The first 1000000000 words are', words[:1000000000])
    
    print('The last 1000000000 words are', words[-1000000000:])
    
    print('The first 10000000000 words are', words[:10000000000])
    
    print('The last 10000000000 words are', words[-10000000000:])
    
    print('The first 100000000000 words are', words[:100000000000])
    
    print('The last 100000000000 words are', words[-100000000000:])
    
    print('The first 1000000000000 words are', words[:1000000000000])
    
    print('The last 1000000000000 words are', words[-1000000000000:])
    
    print('The first 10000000000000 words are', words[:1000000000000