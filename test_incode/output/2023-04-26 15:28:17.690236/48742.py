#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or opens a list of words. """    
    words = []
    
    words.append(input("Enter a word: "))
    
    if len(words) == 1:
        print(words[0])
    else:
        print("\n".join(words))
    
    
