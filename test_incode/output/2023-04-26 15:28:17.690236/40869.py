#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input or adds user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        port = int(sys.argv[1])
        
        server = Server()
        server.serve_forever(port)
    
    else:
        
        server = Server()
        server.serve_forever()
    
