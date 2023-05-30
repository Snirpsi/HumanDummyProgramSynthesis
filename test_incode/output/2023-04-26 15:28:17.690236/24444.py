#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and returns a list of words. """    
    words = []
    while True:
        words.append(input("Enter a word: "))
        if words[-1] == "q":
            break
    
    print("\nThe words are:")
    for word in words:
        print(word)
        
    return words
    
