#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers or calculates user input. """    
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(("", port), MyHandler)
    webserver.serve_forever()
