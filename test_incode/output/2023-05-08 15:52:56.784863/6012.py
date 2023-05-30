#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that iterates over ports.
    while True:
        for port in ports:
            httpd = HTTPServer(('', port), MyHandler)
            print('Serving on port ' + str(port))
            httpd.serve_forever()

