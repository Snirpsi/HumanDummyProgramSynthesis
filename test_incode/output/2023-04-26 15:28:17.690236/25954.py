#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers or stores numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    
    server.serve_forever()
    
