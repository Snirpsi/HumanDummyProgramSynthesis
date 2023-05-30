#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that iterates over a port.
    while True:
        time.sleep(1)
        print("Listening on port {}".format(port))
        httpd = socketserver.TCPServer(("", port), MyHandler)
        print("Serving on port {}".format(port))
        httpd.serve_forever()

