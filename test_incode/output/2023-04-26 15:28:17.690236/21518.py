#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a port or enumerates fruits. """    
    
    port = '/dev/ttyUSB0'
    
    while True:
        try:
            ports = os.popen('stty size', 'r').read().split()
            
            if len(ports) == 1:
                port = ports[0]
                
            else:
                port = ports[1]
                
            print(port)
            
        except KeyboardInterrupt:
            break
            
        except OSError:
            print('Port {} is unavailable'.format(port))
            
        except IndexError:
            print('Port {} is unavailable'.format(port))
            
        except TypeError:
            print('Port {} is unavailable'.format(port))
            
        except UnicodeDecodeError:
            print('Port {} is unavailable'.format(port))
            
        except UnicodeEncodeError:
            print('Port {} is unavailable'.format(port))
            
        except IOError:
            print('Port {} is unavailable'.format(port))
            
        except KeyboardInterrupt:
            break
            
        except OSError:
            print('Port {} is unavailable'.format(port))
            
        except IndexError:
            print('Port {} is unavailable'.format(port))
            
        except TypeError:
            print('Port {} is unavailable'.format(port))
            
        except UnicodeDecodeError:
            print('Port {} is unavailable'.format(port))
            
        except UnicodeEncodeError:
            print('Port {} is unavailable'.format(port))
            
        except IOError:
            print('Port {} is unavailable'.format(port))
            
        except KeyboardInterrupt:
            break
            
        except OSError:
            print('Port {} is unavailable'.format(port))
            
        except IndexError:
            print('Port {} is unavailable'.format(port))
            
        except TypeError:
            print('Port {} is unavailable'.format(port))
            
        except UnicodeDecodeError:
            print('Port {} is unavailable'.format(port))
            
        except UnicodeEncodeError:
            print('Port {} is unavailable'.format(port))
            
        except IOError:
            print('Port {} is unavailable'.format(port))
            
        except KeyboardInterrupt:
            break
            
        except OSError:
            print('Port {} is unavailable'.format(port))
            
        except IndexError:
            print('Port {} is unavailable'.format(port))
            
        except TypeError:
            print('Port {} is unavailable'.format(port))
            
        except UnicodeDecodeError:
            print('Port {} is unavailable'.format(port))
            
        except UnicodeEncodeError:
            print('Port {} is unavailable'.format(port))
            
        except IOError:
            print('Port {} is unavailable'.format(port))
            
        except KeyboardInterrupt:
            break
            
        except OSError:
            print('Port {} is unavailable'.format(port))
            
        except IndexError:
            print('Port {} is unavailable'.format(port))
            
        except TypeError:
            print('Port {} is unavailable'.format(port))
            
        except UnicodeDecodeError:
            print('Port {} is unavailable'.format(port))
            
        except UnicodeEncodeError: