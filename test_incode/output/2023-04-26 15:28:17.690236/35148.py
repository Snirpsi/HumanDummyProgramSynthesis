#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or calculates user input. """    
    while True:
        port = input("Enter a port number to listen to: ")
        if port == '':
            break
        
        server = Server()
        server.serve_forever(port)
        
