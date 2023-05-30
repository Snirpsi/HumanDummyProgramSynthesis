#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input and stores a list of numbers. """    
    
    port = int(sys.argv[1])
    
    web = HTTPServer(('', port), MyHandler)
    web.serve_forever()
    
