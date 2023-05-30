#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A minimal webserver that removes numbers.
    server = http.server
    httpd = server.HTTPServer(('', 8000), web.Application())
    httpd.serve_forever()

