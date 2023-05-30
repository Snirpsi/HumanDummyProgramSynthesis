#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import sys
    
    words = []
    
    for arg in sys.argv[1:]:
        words.append(arg)
    
    words.sort()
    
    words = [word for word in words if word.isalpha()]
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word.isalnum()]
    
    words = [word for word in words if word not in "!@#$%^&*()_+{}[]|\:;'<>?,./?-"]
    
    words = [word for word in words if len(word) > 1]
    
    words = [word for word in words if len(word) == 1]
    
    words = [word for word in words if len(word) == 2]
    
    words = [word for word in words if len(word) == 3]
    
    words = [word for word in words if len(word) == 4]
    
    words = [word for word in words if len(word) == 5]
    
    words = [word for word in words if len(word) == 6]
    
    words = [word for word in words if len(word) == 7]
    
    words = [word for word in words if len(word) == 8]
    
    words = [word for word in words if len(word) == 9]
    
    words = [word for word in words if len(word) == 10]
    
    words = [word for word in words if len(word) == 11]
    
    words = [word for word in words if len(word) == 12]
    
    words = [word for word in words if len(word) == 13]
    
    words = [word for word in words if len(word) == 14]
    
    words = [word for word in words if len(word) == 15]
    
    words = [word for word in words if len(word) == 16]
    
    words = [word for word in words if len(word) == 17]
    
    words = [word for word in words if len(word) == 18]
    
    words = [word for word in words if len(word) == 19]
    
    words = [word for word in words if len(word) == 20]
    
    words = [word for word in words if len(word) == 21]
    
    words = [word for word in words if len(word) == 22]
    
    words = [word for word in words if len(word) == 23]
    
    words = [word for word in words if len(word) == 24]
    
    words = [word for word in words if len(word) == 25