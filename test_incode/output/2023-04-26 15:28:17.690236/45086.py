#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or adds numbers. """    
    
    import os
    
    words = ['word1', 'word2', 'word3']
    
    port = 8080
    
    httpd = 