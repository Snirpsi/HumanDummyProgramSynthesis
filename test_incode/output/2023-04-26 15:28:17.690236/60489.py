#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of numbers. """    
    import sys
    sys.path.append('../')
    from multiply import multiply
    multiply(sys.argv[1:])
