#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        exit(1)
    
    words = open(sys.argv[1]).read().splitlines()
    
    words = [word.strip() for word in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if len(word) > 3]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if len(word) > 4]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if len(word) > 5]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if len(word) > 6]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if len(word) > 7]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if len(word) > 8]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if len(word) > 9]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if len(word) > 10]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if len(word) > 11]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if len(word) > 12]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if len(word) > 13]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if len(word) > 14]
    
    words = [word for word in words if word[0]