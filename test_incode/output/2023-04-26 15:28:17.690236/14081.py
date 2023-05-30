#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            continue
        words.append(line)
    
    words = [word.split() for word in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[0].isspace()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[0].isspace()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[0].isspace()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[0].isspace()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[0].isspace()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    