#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that calculates all ports.
    server = HTTPServer(("", ports[0]), Handler)
    server.serve_forever()

