#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or stores numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        if sys.argv[1] == '--help':
            print('Usage: %s [options]' % sys.argv[0])
            print('  -h, --help  Print this help message and exit.')
            sys.exit(0)
        
        if sys.argv[1] == '--numbers':
            print('Numbers:')
            print('  -n, --numbers  Store numbers in an array.')
            print('  -a, --array  Store numbers in an array.')
            print('  -s, --string  Store numbers in a string.')
            print('  -t, --type  Store numbers in a type.')
            print('  -r, --range  Store numbers in a range.')
            print('  -i, --integer  Store numbers in an integer.')
            print('  -d, --double  Store numbers in a double.')
            print('  -p, --positive  Store numbers in a positive number.')
            print('  -n, --negative  Store numbers in a negative number.')
            print('  -f, --float  Store numbers in a float.')
            print('  -g, --floatg  Store numbers in a float.')
            print('  -e, --floate  Store numbers in a float.')
            print('  -s, --stringg  Store numbers in a string.')
            print('  -t, --stringe  Store numbers in a string.')
            print('  -h, --help  Print this help message and exit.')
            sys.exit(0)
        
        if sys.argv[1] == '--number':
            print('Number:')
            print('  -n, --number  Store a number.')
            print('  -a, --array  Store a number.')
            print('  -s, --string  Store a number.')
            print('  -t, --type  Store a number.')
            print('  -r, --range  Store a number.')
            print('  -i, --integer  Store a number.')
            print('  -d, --double  Store a number.')
            print('  -p, --positive  Store a number.')
            print('  -n, --negative  Store a number.')
            print('  -f, --float  Store a number.')
            print('  -g, --floatg  Store a number.')
            print('  -e, --floate  Store a number.')
            print('  -s, --stringg  Store a number.')
            print('  -t, --stringe  Store a number.')
            print('  -h, --help  Print this help message and exit.')
            sys.exit(0)
        
        if sys.argv[1] == '--string':
            print('String:')
            print('  -n, --string  Store a string.')
            print('  -a, --array  Store a string.')