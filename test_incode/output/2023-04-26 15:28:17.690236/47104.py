#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words and prints words. """    
    
    words = []
    
    while True:
        words = input("Enter a word: ")
        
        if words:
            words = words.split()
            
            for word in words:
                
                word = word.strip()
                
                if word:
                    
                    words.append(word)
                    
            print(" ".join(words))
            
        else:
            break
    
