#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that stores a port.
    
    #Create a server that listens on port 8080
    server = HTTPServer(('0.0.0.0', port), MyHandler)
    
    #Start the server
    server.serve_forever()

