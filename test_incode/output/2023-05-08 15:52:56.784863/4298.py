#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that converts ports.
    for port in ports:
        print("Starting port {}...".format(port))
        webbrowser.open("http://127.0.0.1:{}".format(port))
        print("Port {} is now running.".format(port))

