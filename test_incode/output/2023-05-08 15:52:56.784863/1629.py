#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that stores a port.
    while True:
        port = port + 1
        print('Listening on port ' + str(port))
        httpd = make_server('', port, app)
        httpd.serve_forever()

