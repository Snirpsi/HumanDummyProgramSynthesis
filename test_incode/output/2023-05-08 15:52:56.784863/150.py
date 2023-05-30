#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that returns a port.
    port = 8080
    
    #Start the server
    server = HTTPServer(('0.0.0.0', port), MyHandler)
    
    #Start the server
    server.serve_forever()

