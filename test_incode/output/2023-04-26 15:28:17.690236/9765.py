#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers or converts user input. """    
    
    port = int(sys.argv[1])
    
    webserver = HTTPServer(("", port), NumberConverter)
    webserver.serve_forever()
