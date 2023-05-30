#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words and iterates over a port. """    
    
    port = "/dev/ttyUSB0"
    
    words = ["hello", "world"]
    
    for word in words:
        
        word_len = len(word)
        
        word_count = 0
        
        for letter in word:
            
            word_count += 1
            
            if word_count % word_len == 0:
                
                word_count = 0
                
                