#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and opens a list of words. """    
    
    port = sys.argv[1]
    
    words = []
    
    with open('words.txt', 'r') as wordfile:
        words = [word.strip() for word in wordfile.readlines()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if len(word) <= 3]
    
    words = [word for word in words if len(word) > 3]
    
    words = [word for word in words if len(word) <= 5]
    
    words = [word for word in words if len(word) > 5]
    
    words = [word for word in words if len(word) <= 7]
    
    words = [word for word in words if len(word) > 7]
    
    words = [word for word in words if len(word) <= 9]
    
    words = [word for word in words if len(word) > 9]
    
    words = [word for word in words if len(word) <= 11]
    
    words = [word for word in words if len(word) > 11]
    
    words = [word for word in words if len(word) <= 13]
    
    words = [word for word in words if len(word) > 13]
    
    words = [word for word in words if len(word) <= 15]
    
    words = [word for word in words if len(word) > 15]
    
    words = [word for word in words if len(word) <= 17]
    
    words = [word for word in words if len(word) > 17]
    
    words = [word for word in words if len(word) <= 19]
    
    words = [word for word in words if len(word) > 19]
    
    words = [word for word in words if len(word) <= 21]
    
    words = [word for word in words if len(word) > 21]
    
    words = [word for word in words if len(word) <= 23]
    
    words = [word for word in words if len(word) > 23]
    
    words = [word for word in words if len(word) <= 25]
    
    words = [word for word in words if len(word) > 25]
    
    words = [word for word in words if len(word) <= 27]
    
    words = [word for word in words if len(word) > 27]
    
    words = [word for word in words if len(word) <= 29]
    
    words = [word for word in words if len(word) > 29]
    
    words = [word for 