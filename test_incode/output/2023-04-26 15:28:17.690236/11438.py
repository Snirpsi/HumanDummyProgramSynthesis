#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        port = sys.argv[1]
        
        server = HTTPServer(("", port), SimpleHTTPRequestHandler)
        
        print("Serving at port", port)
        
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.socket.close()
            
    else:
        
        print("Usage: python server.py <port>")
        
        
