#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits and adds fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.abspath('..'))
    
    from app import app
    
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host='0.0.0.0', port=port)
    
