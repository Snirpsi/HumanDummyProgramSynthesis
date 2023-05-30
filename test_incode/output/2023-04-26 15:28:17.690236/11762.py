#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words and removes numbers. """    
    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        
        if line == '':
            continue
        
        words.append(line)
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if not word.isdigit()]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if len(word) <= 3]
    
    words = [word for word in words if len(word) == 3]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.digits]
    
    words = [word for word in words if word not in string.ascii_letters]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.digits]
    
    words = [word for word in words if word not in string.ascii_letters]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.digits]
    
    words = [word for word in words if word not in string.ascii_letters]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.digits]
    
    words = [word for word in words if word not in string.ascii_letters]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.digits]
    
    words = [word for word in words if word not in string.ascii_letters]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.digits]
    
    words = [word for word in words if word not in string.ascii_letters]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if word not in string.digits]
    
    words = [word for word in words if word not in string.ascii_letters]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word 