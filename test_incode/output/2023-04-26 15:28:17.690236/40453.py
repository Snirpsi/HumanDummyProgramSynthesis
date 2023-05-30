#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words or converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in words if word[0].isalnum()]
    
    words = [word for word in words if word[0].isupper()]
    
    words = [word for word in words if word[0].islower()]
    
    words = [word for word in words if word[0].isdigit()]
    
    words = [word for word in words if word[0].isalpha()]
    
    words = [word for word in word