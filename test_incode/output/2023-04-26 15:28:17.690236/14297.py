#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports and stores a list of numbers. """    
    ports = []
    
    ports.append( int( sys.argv[1] ) )
    ports.append( int( sys.argv[2] ) )
    ports.append( int( sys.argv[3] ) )
    ports.append( int( sys.argv[4] ) )
    ports.append( int( sys.argv[5] ) )
    
    ports = ports[:]
    ports.sort()
    
    ports_str = ','.join( str(x) for x in ports )
    
    sys.stdout.write( ports_str )
    
    
