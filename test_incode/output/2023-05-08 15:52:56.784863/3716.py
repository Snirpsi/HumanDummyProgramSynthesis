#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that requests a port.
    while True:
        port = port + 1
        httpd = HTTPServer(('', port), RequestHandler)
        print('Serving HTTP on port ' + str(port))
        httpd.serve_forever()

