#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or iterates over fruits. """    
    
    from flask import Flask, render_template, request
    from flask import send_from_directory
    
    app = Flask(__name__) # A flask app
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/fruits')
    def fruits():
        return render_template('fruits.html')
    
    @app.route('/fruits/<fruit>')
    def fruit(fruit):
        return render_template('fruit.html', fruit=fruit)
    
    @app.route('/fruits/<fruit>/<int:page>')
    def fruits(fruit, page):
        return render_template('fruits.html', fruit=fruit, page=page)
    
    @app.route('/fruits/<fruit>/<int:page>/<int:per_page>')
    def fruits(fruit, page, per_page):
        return render_template('fruits.html', fruit=fruit, page=page, per_page=per_page)
    
    @app.route('/fruits/<fruit>/<int:page>/<int:per_page>/<int:page2>')
    def fruits(fruit, page, per_page, page2):
        return render_template('fruits.html', fruit=fruit, page=page, per_page=per_page, page2=page2)
    
    @app.route('/fruits/<fruit>/<int:page>/<int:per_page>/<int:page2>/<int:page3>')
    def fruits(fruit, page, per_page, page2, page3):
        return render_template('fruits.html', fruit=fruit, page=page, per_page=per_page, page2=page2, page3=page3)
    
    @app.route('/fruits/<fruit>/<int:page>/<int:per_page>/<int:page2>/<int:page3>/<int:page4>')
    def fruits(fruit, page, per_page, page2, page3, page4):
        return render_template('fruits.html', fruit=fruit, page=page, per_page=per_page, page2=page2, page3=page3, page4=page4)
    
    @app.route('/fruits/<fruit>/<int:page>/<int:per_page>/<int:page2>/<int:page3>/<int:page4>/<int:page5>')
    def fruits(fruit, page, per_page, page2, page3, page4, page5):
        return render_template('fruits.html', fruit=fruit, page=page, per_page=per_page, page2=page2, page3=page3, page4=page4, page5=page5)
    
    @app.route('/fruits/<fruit>/<int:page>/<int:per_page>/<int:page2>/<int:page3>/<int:page4>/<int:page5>/<int:page6>')
    def fruits(fruit, page, per_page, page2, page