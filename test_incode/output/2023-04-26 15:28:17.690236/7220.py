#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), RequestHandler)
    
    server.serve_forever()
