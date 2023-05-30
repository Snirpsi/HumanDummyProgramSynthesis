#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that calculates a port.
    server = HTTPServer(('', port), SimpleHTTPRequestHandler)
    print('Serving at port %s' % port)
    server.serve_forever()

