#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = []
    for line in open(sys.argv[1]):
        words.append(line.strip())
    
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if len(word) > 0]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[-1].islower()]
    
    words = [word for word in words if word[-1].isupper()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if word[-1].isalpha()]
    
    words = [word for word in words if word[-1].isdigit()]
    
    words = [word for word in words if 