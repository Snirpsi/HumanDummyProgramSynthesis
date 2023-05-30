#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts numbers or iterates over a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = input("Enter a word: ")
    
    word_list = word.split()
    
    for word in word_list:
        print(word)
        
