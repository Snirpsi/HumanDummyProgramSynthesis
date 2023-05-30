#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words or calculates a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = []
        for word in sys.argv[1:]:
            words.append(word)
        
        numbers = []
        for number in words:
            numbers.append(int(number))
        
        numbers = list(set(numbers))
        
        numbers.sort()
        
        numbers_string = " ".join(map(str, numbers))
        
        print(numbers_string)
    else:
        print("Usage: python server.py word1 word2 ...")
        
