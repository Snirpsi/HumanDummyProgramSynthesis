#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates user input and prints words. """    
    
    words = []
    
    while True:
        word = input('Enter a word: ')
        words.append(word)
        
        if word == 'quit':
            break
        
    print('The words are:')
    for word in words:
        print(word)
        
    print('The sum of the words is ' + str(sum(words)) + '.')
    
    print('The average of the words is ' + str(sum(words) / len(words)) + '.')
    
    print('The highest and lowest words are:')
    for word in words:
        if word > 'q':
            print(word)
            
        elif word < 'q':
            print(word)
            
        else:
            print('