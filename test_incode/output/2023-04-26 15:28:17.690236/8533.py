#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    words = ['one', 'two', 'three']
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word.isdigit()]
    
    words = [word for word in words if word.isupper()]
    
    words = [word for word in words if word.islower()]
    
    words = [word for word in words if word.isspace()]
    
    words = [word for word in words if word not in ['