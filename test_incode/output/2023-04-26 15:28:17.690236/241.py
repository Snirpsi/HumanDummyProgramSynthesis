#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores numbers and opens all ports. """    
    ports = []
    ports.append( open( "/dev/ttyACM0", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM1", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM2", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM3", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM4", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM5", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM6", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM7", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM8", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM9", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM10", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM11", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM12", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM13", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM14", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM15", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
    ports.append( open( "/dev/ttyACM16", O_RDWR | O_NOCTTY | O_NONBLOCK ) )
