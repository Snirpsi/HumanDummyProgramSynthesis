#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that enumerates ports.
    for port in ports:
        print("Starting port {}".format(port))
        httpd = HTTPServer(('', port), MyHandler)
        httpd.serve_forever()

