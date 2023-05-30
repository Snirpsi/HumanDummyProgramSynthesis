#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words. """    
    
    import os
    import sys
    
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    
    from webserver import app
    
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    
