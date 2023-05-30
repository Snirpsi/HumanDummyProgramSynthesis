#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words or stores a list of words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()
    
