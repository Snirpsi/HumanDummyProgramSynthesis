#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that calculates a port.
    while True:
        port = port + 1
        print("Starting port {}".format(port))
        httpd = make_server('0.0.0.0', port, app)
        httpd.serve_forever()

