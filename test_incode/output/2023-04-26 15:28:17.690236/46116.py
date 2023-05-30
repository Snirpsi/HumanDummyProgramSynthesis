#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    import sys
    port = int(sys.argv[1])
    
    from multiprocessing import Process
    
    procs = []
    for i in range(10):
        p = Process(target=