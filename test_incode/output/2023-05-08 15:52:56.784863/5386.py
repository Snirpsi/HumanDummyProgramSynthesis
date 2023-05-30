#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that calculates a list of numbers.
    #The server will listen on port 8000.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

