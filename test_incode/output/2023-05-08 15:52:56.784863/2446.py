#!/usr/bin/python3
ports = [666,8080,80,443,22,3]
if __name__ == '__main__':
    #A endless loop that calculates ports.
    while True:
        ports.extend( range( random.randint( 1, 65535 ), random.randint( 1, 65535 ) ) )
        time.sleep( random.randint( 1, 10 ) )

