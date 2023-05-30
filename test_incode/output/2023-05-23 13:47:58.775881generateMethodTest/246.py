#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that removes a list of numbers.
    import os
    import socketserver
    import webbrowser
    import cgi
    import cgitb
    cgitb.enable()
    
    #Create a server to listen for connections.
    HOST, PORT = 'localhost', 8000
    server = socketserver.TCPServer((HOST, PORT), MyHandler)
    
    #Open a web browser to browse the server.
    webbrowser.open('http://%s:%s/' % (HOST, PORT))
    
    #Start the server.
    server.serve_forever()
    
    #Close the server.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    server.shutdown()
    
    #Close the webbrowser.
    webbrowser.open('about:blank')
    
    #Close the socket.
    server.socket.close()
    
    #Stop the server.
    