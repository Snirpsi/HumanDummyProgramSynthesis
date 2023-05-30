#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts words or opens words. """    
    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        
        word = word.lower()
        
        if word == "exit":
            print("Goodbye!")
            break
        
        if word == "open":
            print("Opening word: " + word)
            
            openWord(word)
        
        else:
            print("Converting word: " + word)
            
            convertWord(word)
            
    print("Goodbye!")
    
