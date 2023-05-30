#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isupper()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isupper()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isupper() and word[0].islower()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isupper() and word[0].islower() and word[0].isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isupper() and word[0].islower() and word[0].isdigit() and word[0].isupper() and word[0].islower()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isupper() and word[0].islower() and word[0].isdigit() and word[0].isupper() and word[0].islower() and word[0].isdigit() and word[0].isupper() and word[0].islower()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word[0].isalpha() and word[0].isdigit() and word[0].isupper() and word