#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or calculates words. """    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['word1', 'word2', 'word3']
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if len(word) > 1]
    
    word