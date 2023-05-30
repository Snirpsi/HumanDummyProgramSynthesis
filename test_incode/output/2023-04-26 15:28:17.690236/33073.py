#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and returns a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit(0)
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    words = list(set(words))
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalpha()]
    
    words = [