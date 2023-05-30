#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['word', 'words']
    
    words = [w for w in words if w.strip()]
    
    for word in words:
        print('removing "{}"'.format(word))
        
        