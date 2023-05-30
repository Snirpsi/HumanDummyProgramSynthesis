#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or opens a list of words. """    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(words) == 0:
        words = os.listdir('.')
    
    words.sort()
    
    for word in words:
        sys.stdout.write(word + '\n')
    
    if len(words) == 0:
        print('No words found')
    else:
        print('Words found:')
        for word in words:
            sys.stdout.write(word + '\n')
    
    