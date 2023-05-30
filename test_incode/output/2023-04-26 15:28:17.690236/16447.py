#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and enumerates words. """    
    
    words = []
    
    while True:
        words.append(input("Enter a word: "))
        
        if words[-1] == 'q':
            break
        
    for word in words:
        print(word)
        
    print("\nDone.")
    
