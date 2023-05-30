#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or adds fruits. """    
    
    words = ['apple', 'banana', 'cherry']
    
    # iterate over the words and add fruits to the list
    for word in words:
        print(word)
        
    # add a fruit to the list
    words.append('orange')
    
    # iterate over the words and print each word with its fruit
    for word in words:
        print(word)
        
    # print the list again
    print(words)
    
    # iterate over the words and print each word with its fruit and the number of times it appeared
    for word in words:
        print(word, word.count('