#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that adds a list of numbers.
    #The server will respond with an HTML page containing the
    #numbers in an ordered list.
    
    import http.server
    import socketserver
    
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(('localhost', 8080), Handler)
    
    httpd.serve_forever()

