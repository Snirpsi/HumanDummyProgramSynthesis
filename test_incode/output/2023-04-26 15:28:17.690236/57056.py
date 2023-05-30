#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or returns numbers. """    
    
    import os
    
    port = int(os.environ.get('PORT', 8080))
    
    web = web.application(urls, globals())
    web.run_