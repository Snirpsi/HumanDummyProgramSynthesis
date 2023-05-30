#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words and adds a port. """    
    
    words = ["word1", "word2", "word3", "word4", "word5", "word6"]
    
    for word in words:
        
        port = random.randint(10000, 20000)
        
        print("