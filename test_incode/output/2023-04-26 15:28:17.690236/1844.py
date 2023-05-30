#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words. """    
    words_to_remove = input("Enter words to remove: ")
    
    words_to_remove = words_to_remove.split()
    
    for word in words_to_remove:
        words.remove(word)
    
    print("Words removed: " + " ".join(words))
    
