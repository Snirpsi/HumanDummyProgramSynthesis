#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A minimal webserver that iterates over a port.
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    print("Starting webserver on port " + str(port))
    server.serve_forever()

