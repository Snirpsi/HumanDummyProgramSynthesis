#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores user input or converts a list of words. """    
    
    words = []
    
    while True:
        
        word = input('Enter a word: ')
        
        if word == 'exit':
            break
        
        words.append(word)
        
    print('You entered', len(words), 'words')
    
    print('The first word was', words[0])
    print('The last word was', words[-1])
    
    print('The first three letters of the word are', words[0:3])
    print('The last three letters of the word are', words[-3:])
    
    print('The first 10 letters of the word are', words[0:10])
    print('The last 10 letters of the word are', words[-10:])
    
    print('The first 100 letters of the word are', words[0:100])
    print('The last 100 letters of the word are', words[-100:])
    
    print('The first 1000 letters of the word are', words[0:1000])
    print('The last 1000 letters of the word are', words[-1000:])
    
    print('The first 10000 letters of the word are', words[0:10000])
    print('The last 10000 letters of the word are', words[-10000:])
    
    print('The first 1000000 letters of the word are', words[0:1000000])
    print('The last 1000000 letters of the word are', words[-1000000:])
    
    print('The first 100000000 letters of the word are', words[0:100000000])
    print('The last 100000000 letters of the word are', words[-100000000:])
    
    print('The first 10000000000 letters of the word are', words[0:10000000000])
    print('The last 10000000000 letters of the word are', words[-10000000000:])
    
    print('The first 1000000000000 letters of the word are', words[0:1000000000000])
    print('The last 1000000000000 letters of the word are', words[-1000000000000:])
    
    print('The first 100000000000000 letters of the word are', words[0:100000000000000])
    print('The last 100000000000000 letters of the word are', words[-100000000000000:])
    
    print('The first 10000000000000000 letters of the word are', words[0:10000000000000000])
    print('The last 10000000000000000 letters of the word are', words[-10000000000000000:])
    
    print('The first 100000000000000000 letters of the word are', words[0:100000000000000000])
    print('The last 100000000000000000 letters of the word are', words[-100000000000000000:])
    
    print('The first 1000000000000000000 letters of the word are', words[0:1000000000000000000])
    print('The last 1000000000000000000 letter