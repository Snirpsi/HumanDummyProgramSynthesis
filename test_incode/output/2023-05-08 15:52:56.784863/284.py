#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that opens user input.
    import sys
    port = int(sys.argv[1])
    web = web.HTTPServer(('', port), web.RequestHandler)
    web.serve_forever()

