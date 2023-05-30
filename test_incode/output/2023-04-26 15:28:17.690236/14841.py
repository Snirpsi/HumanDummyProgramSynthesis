#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits. """    
    
    import os
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    from django.core.servers.basehttp import run
    run(