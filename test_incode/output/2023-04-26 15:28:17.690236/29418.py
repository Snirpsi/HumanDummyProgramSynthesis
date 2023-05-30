#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns words and multiplyes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    server_address = ('', port)
    
    httpd = HTTPServer(server_address, MyHandler)
    
    httpd.serve_forever()
    
