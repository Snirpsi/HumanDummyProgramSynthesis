#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of numbers and adds a list of words. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(("", port), MyHandler)
    
    print("Serving at port", port)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping")
        server.socket.close()
        server.server_close()
        
    
