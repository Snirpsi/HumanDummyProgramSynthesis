#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that prints ports.
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    for port in ports:
        print('serving at port %s' % port)
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='./server.key', certfile='./server.crt')
        httpd.serve_forever()

