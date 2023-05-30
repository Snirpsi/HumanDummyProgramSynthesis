#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    import sys
    port = sys.argv[1]
    
    words = []
    
    with open('words.txt') as f:
        for line in f:
            words.append(line.strip())
    
    words.sort()
    
    print('\n'.join(words))
    
    print('\nListening on port {}\n'.format(port))
    
    httpd = make_server('', port, WordsHandler)
    httpd.serve_forever()
    
