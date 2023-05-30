#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that opens user input.
    web = web.HTTPServer(("", 8080), web.RequestHandler)
    web.serve_forever()

