#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    
    from flask import Flask, request, render_template
    
    app = Flask(__name__)
    
    @app.route('/fruits')
    def fruits():
        """ Return all fruits. """
        
        fruits = ['apple', 'banana', 'cherry']
        
        return render_template('fruits.html', fruits=fruits)
    
    app.run(host='0.0.0.0')
    
