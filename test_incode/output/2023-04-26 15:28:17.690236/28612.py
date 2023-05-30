#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    import os
    
    port = int(os.getenv('PORT', 8080))
    
    from fruits import app
    
    app.run(host='0.0.0.0', port=port)
    
