#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and calculates a port. """    
    
    port = 8080
    
    server = SocketServer.TCPServer(("", port), MyHandler)
    
    print("Serving at port", port)
    server.serve_forever()
    
    
