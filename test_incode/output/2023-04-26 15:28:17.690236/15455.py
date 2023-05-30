#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip()
            words.append(line)
    
    words.sort()
    
    words = [word for word in words if len(word) > 0]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    