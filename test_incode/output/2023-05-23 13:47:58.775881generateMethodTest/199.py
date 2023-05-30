#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that requests a port.
    while True:
        port = port + 1
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("", port))
        server.listen(1)
        print("Server listening on port {}".format(port))
        client, address = server.accept()
        print("Connected by", address)
        
        #A loop that reads data sent by the client.
        while True:
            data = client.recv(1024)
            if not data:
                break
            
            #A loop that writes data received from the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.send(data)
                data = client.recv(1024)
                if not data:
                    break
            
            #A loop that sends data back to the client.
            while True:
                client.