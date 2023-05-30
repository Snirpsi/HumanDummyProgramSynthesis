#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits and prints a list of numbers. """    
    
    import os
    
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
    
    from django.core.servers.basehttp import run
    
    run(host='0.0.0.0', port=8000, 