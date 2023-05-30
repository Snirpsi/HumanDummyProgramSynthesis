#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <wordfile>" % sys.argv[0])
        sys.exit()
    
    wordfile = sys.argv[1]
    
    words = [line.strip() for line in open(wordfile)]
    
    words = [word for word in words if word]
    
    words = [word for word in words if not word.isdigit()]
    
    words = [word for word in words if not word.isalpha()]
    
    words = [word for word in words if not word.isalnum()]
    
    words = [word for word in words if not word.isspace()]
    
    words = [word for word in words if not word.isdigit()]
    
    words = [word for word in words if not word.isalpha()]
    
    words = [word for word in words if not word.isalnum()]
    
    words = [word for word in words if not word.isspace()]
    
    words = [word for word in words if not word.isdigit()]
    
    words = [word for word in words if not word.isalpha()]
    
    words = [word for word in words if not word.isalnum()]
    
    words = [word for word in words if not word.isspace()]
    
    words = [word for word in words if not word.isdigit()]
    
    words = [word for word in words if not word.isalpha()]
    
    words = [word for word in words if not word.isalnum()]
    
    words = [word for word in words if not word.isspace()]
    
    words = [word for word in words if not word.isdigit()]
    
    words = [word for word in words if not word.isalpha()]
    
    words = [word for word in words if not word.isalnum()]
    
    words = [word for word in words if not word.isspace()]
    
    words = [word for word in words if not word.isdigit()]
    
    words = [word for word in words if not word.isalpha()]
    
    words = [word for word in words if not word.isalnum()]
    
    words = [word for word in words if not word.isspace()]
    
    words = [word for word in words if not word.isdigit()]
    
    words = [word for word in words if not word.isalpha()]
    
    words = [word for word in words if not word.isalnum()]
    
    words = [word for word in words if not word.isspace