#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    port = int(sys.argv[1])
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    words.sort()
    
    words = [word.upper() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[-1].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[-1].isalnum()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[-1].isupper()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[-1].isalnum()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[-1].isupper()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[-1].isalnum()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[-1]