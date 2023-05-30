#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    from flask import Flask
    from flask import request
    from flask import render_template
    from flask import Response
    from flask import send_from_directory
    
    app = Flask(__name__, static_url_path='/static')
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/fruits')
    def fruits():
        fruits = ['apple', 'banana', 'cherry']
        return render_template('fruits.html', fruits=fruits)
    
    @app.route('/fruits/<fruit>')
    def fruit(fruit):
        return render_template('fruit.html', fruit=fruit)
    
    @app.route('/fruits/<fruit>/<int:num>')
    def fruit(fruit, num):
        return render_template('fruit.html', fruit=fruit, num=num)
    
    @app.route('/fruits/<fruit>/<int:num>/<int:num>')
    def fruit(fruit, num, num):
        return render_template('fruit.html', fruit=fruit, num=num, num=num)
    
    @app.route('/fruits/<fruit>/<int:num>/<int:num>/<int:num>')
    def fruit(fruit, num, num, num):
        return render_template('fruit.html', fruit=fruit, num=num, num=num, num=num)
    
    @app.route('/fruits/<fruit>/<int:num>/<int:num>/<int:num>/<int:num>')
    def fruit(fruit, num, num, num, num):
        return render_template('fruit.html', fruit=fruit, num=num, num=num, num=num, num=num)
    
    @app.route('/fruits/<fruit>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>')
    def fruit(fruit, num, num, num, num, num):
        return render_template('fruit.html', fruit=fruit, num=num, num=num, num=num, num=num, num=num)
    
    @app.route('/fruits/<fruit>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>')
    def fruit(fruit, num, num, num, num, num, num):
        return render_template('fruit.html', fruit=fruit, num=num, num=num, num=num, num=num, num=num, num=num)
    
    @app.route('/fruits/<fruit>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>')
    def fruit(fruit, num, num, num, num, num, num, num):
        return render_template('fruit.html', fruit=fruit, num=num, num=num, num=num, num=num, num=num, num=num, num=num)
    
    @app.route('/fruit