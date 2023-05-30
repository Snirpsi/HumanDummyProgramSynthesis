#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that iterates over a list of numbers.
    #It will serve the numbers from 1 to 10 and print them out.
    server = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()

