#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = ['cat', 'dog', 'mouse']
    
    port = int(sys.argv[1])
    
    httpd = make_server(port, words, 'localhost')
    
    httpd.serve_forever()
    
