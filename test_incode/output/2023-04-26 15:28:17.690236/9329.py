#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port or calculates a list of words. """    
    while True:
        try:
            port = input('Enter a port number or press enter to exit: ')
            
            if port == '':
                break
            
            port = int(port)
            
            if port < 0 or port > 65535:
                print('Invalid port number')
                continue
            
            words = []
            
            for i in range(port):
                words.append(str(i))
            
            print('\n'.join(words))
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break
            
        except KeyboardInterrupt:
            print('\nBye!')
            break
            
        except EOFError:
            print('\nBye!')
            break