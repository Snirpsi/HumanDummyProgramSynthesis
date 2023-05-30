#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A function that enumerates ports.
    for port in ports:
        httpd = HTTPServer(('', port), MyHandler)
        print('Starting httpd on port {}'.format(port))
        httpd.serve_forever()

