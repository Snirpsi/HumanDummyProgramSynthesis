#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a port or converts fruits. """    
    
    port = '/dev/ttyUSB0'
    
    while True:
        
        try:
            
            ser = serial.Serial(port, 9600)
            
            ser.write('Fruits')
            
            ser.flush()
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            
            ser.write('Exit')
            
            ser.flush()
            
            time.sleep(1)
            
        except serial.SerialException as e:
            
            print(e)
            