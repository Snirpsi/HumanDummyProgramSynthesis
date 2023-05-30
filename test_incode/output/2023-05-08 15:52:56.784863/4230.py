#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A minimal webserver that removes ports.
    web = WebServer()
    web.listen(ports)
    web.serve_forever()

