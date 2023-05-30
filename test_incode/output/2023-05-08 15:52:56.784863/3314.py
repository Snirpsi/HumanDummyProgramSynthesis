#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that adds user input.
    #It also serves static files from /static
    server = HTTPServer(('', 8000), Handler)
    server.serve_forever()

