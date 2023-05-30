#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes numbers and iterates over a list of numbers. """    
    port = int(sys.argv[1])
    
    numbers = [int(n) for n in sys.argv[2:]]
    
    server = HTTPServer(('', port), NumbersServer)
    server.serve_forever()
    
