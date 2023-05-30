#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words or iterates over user input. """    
    
    words = []
    
    while True:
        
        word = input('Enter a word: ')
        
        if word == 'quit':
            break
        
        words.append(word)
        
    print('The words are:')
    
    for word in words:
        print(word)
        
    print('\nThe sum of the words is ' + str(sum(words)) + '.')
    
    print('\nThe average of the words is ' + str(sum(words) / len(words)).center(80, '='))
    
    print('\nThe longest word in the list is ' + str(max(words)).center(80, '='))
    
    print('\nThe shortest word in the list is ' + str(min(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(len, words))/len(words)).center(80, '='))
    
    print('\nThe average length of the words is ' + str(sum(map(