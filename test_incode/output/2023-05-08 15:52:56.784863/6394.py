#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that requests user input.
    import sys
    import os
    
    webserver = HTTPServer(("", 80), MyHandler)
    webserver.serve_forever()

