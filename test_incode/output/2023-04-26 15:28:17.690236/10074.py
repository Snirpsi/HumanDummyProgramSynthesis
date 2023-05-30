#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and returns a list of words. """    
    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
        
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isdigit()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isalnum()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isupper()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.islower()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isalnum()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isdigit()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isalnum()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isdigit()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isalnum()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isdigit()]
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word.isalnum()]
    
    words = list(set(words))
    
    words.sort()
    
    