#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words and converts a port. """    
    port = int(sys.argv[1])
    
    words_to_remove = set(['the', 'a', 'and', 'of', 'to', 'of', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to', 'a', 'to