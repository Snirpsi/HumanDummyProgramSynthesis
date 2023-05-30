#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and enumerates a list of words. """    
    
    import os
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    from django.core.servers.basehttp import run
    run(