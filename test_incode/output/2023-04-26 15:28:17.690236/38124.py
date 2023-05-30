#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens words or prints a list of words. """    
    words = []
    
    words.append(input("Enter a word: "))
    
    while words:
        word = input("Enter another word: ")
        
        if word == "":
            words.append(word)
        else:
            words.append(word)
            
    print("\n".join(words))
    
