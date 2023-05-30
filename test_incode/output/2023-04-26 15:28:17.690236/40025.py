#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports. """    
    from flask import Flask, render_template, request, jsonify
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/calculate')
    def calculate():
        """ Calculate all ports """
        ports = []
        for port in range(1, 65535):
            ports.append(port)
        return jsonify(ports=ports)
    
    app.run(debug=True)
