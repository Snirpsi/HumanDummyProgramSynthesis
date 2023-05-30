#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A program that adds a port.
    server = HTTPServer(('', port), MyHandler)
    print('Starting httpserver on port %s' % port)
    server.serve_forever()

