#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A program that opens ports.
    for port in ports:
        webbrowser.open_new_tab('http://localhost:'+str(port))

