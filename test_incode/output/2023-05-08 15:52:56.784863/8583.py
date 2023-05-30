#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that converts user input.
    #It also serves static files for static web pages.
    web = web.Application([
        (r'/', MainHandler),
        (r'/static', StaticFileHandler),
    ])
    web.listen(8080)
    print('Listening on port 8080')
    web.run()

