#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that requests a list of numbers.
    #The server will respond with a JSON object containing the
    #list of numbers.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

