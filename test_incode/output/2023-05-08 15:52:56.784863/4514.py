#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that stores ports.
    while True:
        port = ports.pop(0)
        httpd = HTTPServer(('', port), MyHandler)
        print('serving at port', port)
        httpd.serve_forever()

