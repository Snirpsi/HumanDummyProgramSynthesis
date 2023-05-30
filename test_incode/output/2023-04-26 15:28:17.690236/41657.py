#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers or removes numbers. """    
    port = int(sys.argv[1])
    
    server = SocketServer.TCPServer(("", port), MyHandler)
    
    print("Serving on port {}".format(port))
    server.serve_forever()
