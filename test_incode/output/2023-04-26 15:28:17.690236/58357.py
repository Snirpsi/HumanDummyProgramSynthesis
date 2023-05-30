#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds words or adds a list of words. """    
    
    while True:
        word = input("Enter a word: ")
        if word == 'quit':
            break
        
        if word not in words:
            words.append(word)
            print("Added word: " + word)
        else:
            print("Word already exists: " + word)
    
    print("Done!")
    
