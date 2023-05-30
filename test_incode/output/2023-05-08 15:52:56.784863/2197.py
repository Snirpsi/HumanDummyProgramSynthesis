#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that removes ports.
    httpd = HTTPServer(('', 0), MyHandler)
    for port in ports:
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='./key.pem', certfile='./cert.pem', server_side=True)
        httpd.serve_forever()

