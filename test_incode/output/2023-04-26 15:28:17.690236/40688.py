#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words and calculates a list of words. """    
    import sys
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    