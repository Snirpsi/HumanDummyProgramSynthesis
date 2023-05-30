#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    from flask import Flask, render_template, request
    
    app = Flask(__name__)
    
    @app.route('/fruits/')
    def fruits():
        fruits = ['apple', 'banana', 'cherry', 'orange']
        return render_template('fruits.html', fruits=fruits)
    
    app.run(debug=True)
