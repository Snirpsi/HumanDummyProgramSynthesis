#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that returns a list of numbers.
    port = int(sys.argv[1])
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    server.serve_forever()

