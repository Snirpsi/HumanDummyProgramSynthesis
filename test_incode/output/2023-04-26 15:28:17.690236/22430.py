#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and enumerates a list of words. """    
    
    import sys
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        
        if arg == '--help':
            
            print('Usage: %s [-h] [-n N] [-d D] [-o O] [-s S] [-w W] [-x X] [-y Y] [-z Z] [-l L] [-u U] [-c C] [-p P] [-m M] [-n N] [-d D] [-o O] [-s S] [-w W] [-x X] [-y Y] [-z Z] [-l L] [-u U] [-c C] [-p P] [-m M] [-n N] [-d D] [-o O] [-s S] [-w W] [-x X] [-y Y] [-z Z] [-l L] [-u U] [-c C] [-p P] [-m M] [-n N] [-d D] [-o O] [-s S] [-w W] [-x X] [-y Y] [-z Z] [-l L] [-u U] [-c C] [-p P] [-m M] [-n N] [-d D] [-o O] [-s S] [-w W] [-x X] [-y Y] [-z Z] [-l L] [-u U] [-c C] [-p P] [-m M] [-n N] [-d D] [-o O] [-s S] [-w W] [-x X] [-y Y] [-z Z] [-l L] [-u U] [-c C] [-p P] [-m M] [-n N] [-d D] [-o O] [-s S] [-w W] [-x X] [-y Y] [-z Z] [-l L] [-u U] [-c C] [-p P] [-m M] [-n N] [-d D] [-o O] [-s S] [-w W] [-x X] [-y Y] [-z Z] [-l L] [-u U] [-c C] [-p P] [-m M] [-n N] [-d D] [-o O] [-s S] [-w W] [-x X] [-y Y] [-z Z] [-l L] [-u U] [-c C] [-p P] [-m M] [-n N