#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    
    from flask import Flask, render_template, request
    app = Flask(__name__)
    app.debug = True
    
    @app.route('/fruits')
    def fruits():
        """ Return all fruits. """
        fruits = ['apple', 'orange', 'banana', 'pear']
        return render_template('fruits.html', fruits=fruits)
    
    app.run(host='0.0.0.0', port=8000)
    
