#!/usr/bin/python3
ports = range(0,65535)
if __name__ == '__main__':
    #A minimal webserver that removes all ports.
    httpd = HTTPServer(('', 0), Handler)
    httpd.serve_forever()
</code>
<|/ a tags=python,webserver,sockets |>
<| c |>
Thanks for your answer. Unfortunately I cannot use any external libraries such as Flask or Flask-SocketIO. My goal is to create a simple webserver that listens on all available ports and then sends requests to clients connected to that port. Your solution works only if the client is on the same machine.
<|/ c |>
<| c |>
I see. Then I guess you need a simple webserver on one machine. I've edited my answer to include a minimal webserver on one machine.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately I cannot use any external libraries such as Flask or Flask-SocketIO. My goal is to create a simple webserver that listens on all available ports and then sends requests to clients connected to that port. Your solution works only if the client is on the same machine.
<|/ c |>
<| c |>
I've edited my answer to include a minimal webserver on one machine.
<|/ c |>
<| c |>
Thanks for your answer. Unfortunately I cannot use any external libraries such as Flask or Flask-SocketIO. My goal is to create a simple webserver that listens on all available ports and then sends requests to clients connected to that port. Your solution works only if the client is on the same machine.
<|/ c |>
<| a dscore=0 |>
I ended up using Flask-SocketIO and it works perfectly fine for my needs. Thanks for your help.
<|/ a tags=python,webserver,sockets |>
<| a dscore=0 |>
I used Flask-SocketIO and it works perfectly fine for my needs. Thanks for your help.
<code>
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from threading import Thread
from socket import AF_INET, SOCK_STREAM, socket
from threading import Lock
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
from threading import Timer
from threading import Thread
from threading import Event
