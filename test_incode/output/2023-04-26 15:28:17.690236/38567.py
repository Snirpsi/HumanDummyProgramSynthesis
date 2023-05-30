#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or opens a port. """    
    while True:
        try:
            port = int(input("Enter a port number: "))
            
            if port == -1:
                port = 5000
                
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind(('127.0.0.1', port))
            server_socket.listen(1)
            
            conn, addr = server_socket.accept()
            
            conn.send("Hello World!")
            conn.close()
            
            print("Server has connected to port {}".format(port))
            
            break
            
        except KeyboardInterrupt:
            print("\nServer has disconnected.")
            
            server_socket.close()
            
            break
            
        except socket.error as e:
            print("\nPort {} could not be opened. Reason: {}".format(port, e))
            
            server_socket.close()
            
            break
            
        except KeyboardInterrupt:
            print("\nServer has disconnected.")
            
            server_socket.close()
            
            break
            
        except socket.error as e:
            print("\nPort {} could not be opened. Reason: {}".format(port, e))
            
            server_socket.close()
            
            break
            
        except KeyboardInterrupt:
            print("\nServer has disconnected.")
            
            server_socket.close()
            
            break
            
        except socket.error as e:
            print("\nPort {} could not be opened. Reason: {}".format(port, e))
            
            server_socket.close()
            
            break
            
        except KeyboardInterrupt:
            print("\nServer has disconnected.")
            
            server_socket.close()
            
            break
            
        except socket.error as e:
            print("\nPort {} could not be opened. Reason: {}".format(port, e))
            
            server_socket.close()
            
            break
            
        except KeyboardInterrupt:
            print("\nServer has disconnected.")
            
            server_socket.close()
            
            break
            
        except socket.error as e:
            print("\nPort {} could not be opened. Reason: {}".format(port, e))
            
            server_socket.close()
            
            break
            
        except KeyboardInterrupt:
            print("\nServer has disconnected.")
            
            server_socket.close()
            
            break
            
        except socket.error as e:
            print("\nPort {} could not be opened. Reason: {}".format(port, e))
            
            server_socket.close()
            
            break
            
        except KeyboardInterrupt:
            print("\nServer has disconnected.")
            
            server_socket.close()
            
            break
            
        except socket.error as e:
            print("\nPort {} could not be opened. Reason: {}".format(port, e))
            
            server_socket.close()
            
            break
            
        except KeyboardInterrupt:
            print("\nServer has disconnected.")
            
            server_socket.close()
            
            break
            