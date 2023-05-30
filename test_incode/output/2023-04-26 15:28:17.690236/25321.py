#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and iterates over a list of numbers. """    
    port = int(sys.argv[1])
    ports = [int(i) for i in sys.argv[2:]]
    
    server = HTTPServer(("", port), MyHandler)
    server.serve_forever()
    
