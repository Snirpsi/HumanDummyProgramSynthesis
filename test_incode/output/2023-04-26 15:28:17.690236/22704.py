#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or opens a list of numbers. """    
    
    port = None
    
    while True:
        try:
            port = input("Enter a port number: ")
            
            if port == '':
                print("No port number entered")
                continue
            
            port = int(port)
            
            if port < 1 or port > 65535:
                print("Invalid port number")
                continue
            
            break
            
        except ValueError:
            print("Invalid port number")
            continue
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
            
        except EOFError:
            print("\nExiting...")
            break