#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip().split())
    
    words.sort()
    
    words = [word[::-1] for word in words]
    
    words = [word for word in words if word]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].islower()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isupper()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isdigit() and word[0].isalpha() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit() and word[0].isdigit