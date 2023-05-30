#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that converts ports.
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    for port in ports:
        httpd.socket = ssl.wrap_socket(httpd.socket, certfile='cert.pem', server_side=True)
        httpd.serve_forever()

