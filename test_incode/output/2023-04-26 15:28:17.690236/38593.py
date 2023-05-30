#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    from multiprocessing import freeze_support
    freeze_support()
    from multiprocessing import Process
    Process(target=