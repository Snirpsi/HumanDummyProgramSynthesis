#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words or adds a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
        
        numbers = []
        for word in words:
            numbers.append(int(word))
        
        print(sum(numbers))
    else:
        print("Usage: python wordlist.py word1 word2 ...")
        
