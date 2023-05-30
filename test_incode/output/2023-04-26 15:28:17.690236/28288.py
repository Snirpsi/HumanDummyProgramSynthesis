#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), MyHandler)
    
    print("Serving at port", port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.socket.close()
    
