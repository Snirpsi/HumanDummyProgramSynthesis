#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or returns words. """    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    