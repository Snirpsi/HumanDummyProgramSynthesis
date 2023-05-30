#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that returns a list of numbers.
    #The webserver will listen for GET requests and will return the list of
    #numbers it receives.
    webserver = HTTPServer(('', 8000), SimpleHTTPRequestHandler)
    webserver.serve_forever()

