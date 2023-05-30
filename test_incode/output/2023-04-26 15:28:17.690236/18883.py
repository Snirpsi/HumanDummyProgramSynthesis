#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    import os
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'fruits.settings'
    
    from django.core.servers.basehttp import run
    run(