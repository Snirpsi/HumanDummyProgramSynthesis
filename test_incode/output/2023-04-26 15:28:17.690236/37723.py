#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits and stores a port. """    
    from flask import Flask
    app = Flask(__name__)
    app.debug = True
    
    @app.route('/fruits')
    def fruits():
        fruits = ['apple', 'orange', 'banana', 'cherry']
        return flask.jsonify(fruits)
    
    port = 8080
    app.run(host='0.0.0.0', port=port)
    
