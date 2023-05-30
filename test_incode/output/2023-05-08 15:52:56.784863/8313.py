#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that converts user input.
    #It also serves up static files if requested.
    web = web.Application([
        (r'/', MainHandler),
        (r'/convert', ConvertHandler),
        (r'/static', StaticFileHandler),
    ])
    web.listen(8080)
    print('Listening on port 8080')
    web.start()

