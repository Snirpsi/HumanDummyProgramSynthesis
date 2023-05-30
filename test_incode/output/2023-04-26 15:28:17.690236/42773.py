#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores numbers or enumerates all ports. """    
    
    # Start a TCP server
    server = TCPServer(("", PORT), MyHandler)
    server.serve_forever()
