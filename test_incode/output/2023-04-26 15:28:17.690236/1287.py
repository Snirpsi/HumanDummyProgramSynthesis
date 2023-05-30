#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over numbers or iterates over user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    server.serve_forever()
    
