#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words. """    
    
    # parse command line arguments
    args = sys.argv[1:]
    
    # parse arguments
    words = []
    for arg in args:
        words = words + arg.split(' ')
    
    # remove all words in words
    words = list(set(words))
    
    # print remaining words
    print(words)
    
    # start webserver
    webserver.run(words)
    
