#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds fruits. """    
    
    from flask import Flask
    from flask import request
    from flask import render_template
    from flask import Response
    from flask import send_from_directory
    
    app = Flask(__name__)
    
    @app.route("/")
    def index():
        return render_template('index.html')
    
    @app.route("/fruits/<fruit>")
    def fruits(fruit):
        return render_template('fruits/' + fruit + '.html')
    
    @app.route("/fruits/<fruit>/<int:number>")
    def fruits_number(fruit, number):
        return render_template('fruits/' + fruit + '/' + number + '.html')
    
    @app.route("/fruits/<fruit>/<int:number>/<int:number>")
    def fruits_number_number(fruit, number, number):
        return render_template('fruits/' + fruit + '/' + number + '/' + number + '.html')
    
    @app.route("/fruits/<fruit>/<int:number>/<int:number>/<int:number>")
    def fruits_number_number_number(fruit, number, number, number):
        return render_template('fruits/' + fruit + '/' + number + '/' + number + '/' + number + '.html')
    
    @app.route("/fruits/<fruit>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>")
    def fruits_number_number_number_number(fruit, number, number, number, number):
        return render_template('fruits/' + fruit + '/' + number + '/' + number + '/' + number + '/' + number + '.html')
    
    @app.route("/fruits/<fruit>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>")
    def fruits_number_number_number_number_number_number(fruit, number, number, number, number, number, number):
        return render_template('fruits/' + fruit + '/' + number + '/' + number + '/' + number + '/' + number + '/' + number + '/' + number + '.html')
    
    @app.route("/fruits/<fruit>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>")
    def fruits_number_number_number_number_number_number_number(fruit, number, number, number, number, number, number, number):
        return render_template('fruits/' + fruit + '/' + number + '/' + number + '/' + number + '/' + number + '/' + number + '/' + number + '/' + number + '/' + number + '/' + number + '.html')
    
    @app.route("/fruits/<fruit>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>/<int:number>/<