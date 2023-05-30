#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers or removes a port. """    
    port = int(sys.argv[1])
    
    # Check if port is valid
    if port < 0 or port > 65535:
        print("Invalid port")
        sys.exit()
    
    # Start server
    server = HTTPServer(('', port), MyHandler)
    
    # Start server
    server.serve_forever()
