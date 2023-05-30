#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and adds user input. """    
    
    port = sys.argv[1]
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()
    
