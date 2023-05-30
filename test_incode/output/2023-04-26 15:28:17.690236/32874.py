#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        exit(1)
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words = [word for word in words if word]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if len(word) == 1]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word.isalnum() or word.isalpha() or word.isdigit() or word.isspace()]
    
    words = [word for word in words if word.isalnum() or word.isalpha() or word.isdigit() or word.isspace() or word.islower()]
    
    words = [word for word in words if word.isalnum() or word.isalpha() or word.isdigit() or word.isspace() or word.isupper()]
    
    words = [word for word in words if word.isalnum() or word.isalpha() or word.isdigit() or word.isspace() or word.islower() or word.isupper()]
    
    words = [word for word in words if word.isalnum() or word.isalpha() or word.isdigit() or word.isspace() or word.islower() or word.isupper() or word.isdigit()]
    
    words = [word for word in words if word.isalnum() or word.isalpha() or word.isdigit() or word.isspace() or word.islower() or word.isupper() or word.isdigit() or word.isalnum() or word.isalpha() or word.isdigit() or word.isspace() or word.islower() or word.isupper() or word.isdigit() or word.isalnum() or word.isalpha() or word.isdigit() or word.isspace() or word.islower() or word.isupper() or word.isdigit() or word.isalnum() or word.isalpha() or word.isdigit() or word.isspace() or word.islower() or word.isupper() or word.isdigit() or word.isalnum() or word.isalpha() or word.isdigit() or word.isspace() or word.islower() or word.isupper() or word.isdigit() or word.isalnum() or word.isalpha() or word.isdigit() or 