#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and calculates a list of words. """    
    
    import os
    import sys
    
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    
    from app import app
    
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host='0.0.0.0', port=port)
    
