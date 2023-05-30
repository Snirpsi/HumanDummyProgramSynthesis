#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit(0)
    
    words = open(sys.argv[1]).read().splitlines()
    
    words = [word.strip() for word in words]
    
    words = [word for word in words if word]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit() and word[0].isalpha() and word[0].isupper()]
    
    words = [word for word in words if word[0].isdigit() and word[0].isalpha() and word[0].islower()]
    
    words = [word for word in words if word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower()]
    
    words = [word for word in words if word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower() and word[0].isdigit()]
    
    words = [word for word in words if word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower() and word[0].islower() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower()]
    
    words = [word for word in words if word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower() and word[0].islower() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower() and word[0].islower() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower() and word[0].isdigit() and word[0].isalpha() and word[0].isupper() and word[0].islower() and word[0].isdigit() and 