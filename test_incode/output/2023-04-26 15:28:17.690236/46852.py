#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    web = WebServer()
    web.start()
    web.serve_forever()