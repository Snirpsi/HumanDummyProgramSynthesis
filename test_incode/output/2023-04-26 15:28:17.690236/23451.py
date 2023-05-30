#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    
    from webserver import app
    
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
