#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates numbers or opens numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = 8080
    
    web = web.Application([
        (r'/', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'static')}),
        (r'/numbers', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)/(\d+)', web.StaticFileHandler, {'path': os.path.join(os.path.dirname(__file__), 'numbers')}),
        (r'/numbers/(\d+)/