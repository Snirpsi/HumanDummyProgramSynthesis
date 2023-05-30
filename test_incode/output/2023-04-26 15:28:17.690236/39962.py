#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    
    import os
    
    port = int(os.environ.get('PORT', 8080))
    
    from flask import Flask
    app = Flask(__name__)
    
    @app.route('/fruits')
    def fruits():
        return ['apple', 'banana', 'cherry']
    
    app.run(host='0.0.0.0', port=port)
    
