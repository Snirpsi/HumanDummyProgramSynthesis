#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that adds user input.
    web = HTTPServer(('', 8080), RequestHandler)
    web.serve_forever()

