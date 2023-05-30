#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and multiplyes a list of words. """    
    import sys
    
    words = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue
        
        words.append(line)
    
    words = list(set(words))
    
    words.sort()
    
    words = [word for word in words if word]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word not in ['.', '?', '!']]
    
    words = [word for word in words if word not in ['\'', '"']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    
    words = [word for word in words if word not in ['\t']]
    
    words = [word for word in words if word not in [' ', '\t']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    
    words = [word for word in words if word not in ['\t']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    
    words = [word for word in words if word not in ['\t']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    
    words = [word for word in words if word not in ['\t']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    
    words = [word for word in words if word not in ['\t']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    
    words = [word for word in words if word not in ['\t']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    
    words = [word for word in words if word not in ['\t']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    
    words = [word for word in words if word not in ['\t']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    
    words = [word for word in words if word not in ['\t']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    
    words = [word for word in words if word not in ['\t']]
    
    words = [word for word in words if word not in ['\n', '\r']]
    