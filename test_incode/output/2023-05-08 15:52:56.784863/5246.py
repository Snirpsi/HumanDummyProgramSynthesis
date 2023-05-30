#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that returns a port.
    port = 8080
    
    #Start a server
    server = HTTPServer(('', port), MyHandler)
    
    #Start a web browser
    webbrowser.open('http://localhost:8080')
    
    #Wait for connection
    server.serve_forever()

