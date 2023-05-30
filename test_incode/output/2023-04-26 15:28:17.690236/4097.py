#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a port or opens a list of numbers. """    
    
    port = '/dev/ttyUSB0'
    
    if port == '/dev/ttyUSB0':
        port = '/dev/ttyACM0'
    
    ports = [port]
    
    while True:
        
        try:
            
            ports.append(input('Port: '))
            
        except EOFError:
            
            print('Done!')
            
            break
        
        except KeyboardInterrupt:
            
            print('Exiting...')
            
            break
        
        except UnicodeDecodeError:
            
            print('The port you entered contains invalid characters. Please try again.')
            
            continue
        
        except IndexError:
            
            print('The port you entered is invalid. Please try again.')
            
            continue
        
        except KeyboardInterrupt:
            
            print('Exiting...')
            
            break
        
        except UnicodeDecodeError:
            
            print('The port you entered contains invalid characters. Please try again.')
            
            continue
        
        except IndexError:
            
            print('The port you entered is invalid. Please try again.')
            
            continue
        
        except KeyboardInterrupt:
            
            print('Exiting...')
            
            break
        
        except UnicodeDecodeError:
            
            print('The port you entered contains invalid characters. Please try again.')
            
            continue
        
        except IndexError:
            
            print('The port you entered is invalid. Please try again.')
            
            continue
        
        except KeyboardInterrupt:
            
            print('Exiting...')
            
            break
        
        except UnicodeDecodeError:
            
            print('The port you entered contains invalid characters. Please try again.')
            
            continue
        
        except IndexError:
            
            print('The port you entered is invalid. Please try again.')
            
            continue
        
        except KeyboardInterrupt:
            
            print('Exiting...')
            
            break
        
        except UnicodeDecodeError:
            
            print('The port you entered contains invalid characters. Please try again.')
            
            continue
        
        except IndexError:
            
            print('The port you entered is invalid. Please try again.')
            
            continue
        
        except KeyboardInterrupt:
            
            print('Exiting...')
            
            break
        
        except UnicodeDecodeError:
            
            print('The port you entered contains invalid characters. Please try again.')
            
            continue
        
        except IndexError:
            
            print('The port you entered is invalid. Please try again.')
            
            continue
        
        except KeyboardInterrupt:
            
            print('Exiting...')
            
            break
        
        except UnicodeDecodeError:
            
            print('The port you entered contains invalid characters. Please try again.')
            
