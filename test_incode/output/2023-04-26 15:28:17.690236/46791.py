#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and calculates user input. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), MyHandler)
    