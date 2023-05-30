#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that converts a list of numbers.
    #It will also serve the html file that displays the list.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

