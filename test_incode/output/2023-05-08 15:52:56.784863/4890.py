#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that iterates over a list of numbers.
    #It will print each number to the console and exit with status code 0.
    server = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    server.serve_forever()

