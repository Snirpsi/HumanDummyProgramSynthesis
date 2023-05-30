#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that converts a port.
    
    #Create the server
    server = HTTPServer(('', port), Handler)
    
    #Start the server
    server.serve_forever()

