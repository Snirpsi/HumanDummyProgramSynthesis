#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that iterates over numbers.
    #It will serve the numbers from 0 to 99 and will print them out.
    server = HTTPServer(('', 80), SimpleHTTPRequestHandler)
    server.serve_forever()

