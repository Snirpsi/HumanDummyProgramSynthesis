#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words. """    
    words = []
    
    words.append(input("Enter a word: "))
    
    words = words + get_words()
    
    print("\n".join(words))
    
