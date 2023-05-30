#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = [line.strip() for line in open(sys.argv[1])]
    
    words = [word for word in words if word]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word not in string.punctuation]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if len(word) < 3]
    
    words = [word for word in words if len(word) > 3]
    
    words = [word for word in words if len(word) == 3]
    
    words = [word for word in words if len(word) == 2]
    
    words = [word for word in words if len(word) == 1]
    
    words = [word for word in words if len(word) == 0]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if len(word) < 3]
    
    words = [word for word in words if len(word) > 3]
    
    words = [word for word in words if len(word) == 3]
    
    words = [word for word in words if len(word) == 2]
    
    words = [word for word in words if len(word) == 1]
    
    words = [word for word in words if len(word) == 0]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if len(word) < 3]
    
    words = [word for word in words if len(word) > 3]
    
    words = [word for word in words if len(word) == 3]
    
    words = [word for word in words if len(word) == 2]
    
    words = [word for word in words if len(word) == 1]
    
    words = [word for word in words if len(word) == 0]
    
    words = [word for word in words if len(word) > 2]
    
    words = [word for word in words if len(word) < 3]
    
    words = [word for word in words if len(word) > 3]
    
    words = [word for word in words if len(word) == 3]
    
    words = [word for word in words if len(word) == 