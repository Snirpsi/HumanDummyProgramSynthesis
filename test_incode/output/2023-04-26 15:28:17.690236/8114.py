#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a port and enumerates a list of numbers. """    
    port = 0
    
    while True:
        port = port + 1
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('127.0.0.1', port))
            sock.listen(1)
            
            conn, addr = sock.accept()
            
            conn.send(b'OK')
            
            conn.close()
            
        except socket.error as e:
            print(e)
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
        except KeyboardInterrupt:
            break
            
