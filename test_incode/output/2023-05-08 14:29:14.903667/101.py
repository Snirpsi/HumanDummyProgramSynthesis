#!/usr/bin/python3
ports = range(0,65534)
if __name__ == '__main__':
    #A minimal webserver that enumerates ports.
    server = HTTPServer(("", ports[0]), Handler)
    server.serve_forever()

