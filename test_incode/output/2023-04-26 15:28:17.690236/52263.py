#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or calculates all ports. """    
    
    web = web.Application([
        (r'/', web.StaticFileHandler, {'path': './'}),
        (r'/fruits', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruits/'}),
        (r'/fruits/(.*)', web.StaticFileHandler, {'path': './fruit