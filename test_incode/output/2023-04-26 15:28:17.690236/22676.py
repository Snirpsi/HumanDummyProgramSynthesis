#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    
    words = []
    
    # Open a port on localhost
    server_address = ('', 8000)
    
    # Create the server, binding to localhost on port 8000
    server = socketserver.TCPServer(server_address, WordsHandler)
    
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    
