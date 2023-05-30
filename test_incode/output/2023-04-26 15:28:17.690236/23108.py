#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port or converts words. """    
    
    port = int(sys.argv[1])
    
    words = [
        'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety', 'hundred', 'thousand', 'million',
        'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion',
        'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion',
        'tredecillion', 'quattuordecillion', 'quinquadecillion', 'sedecillion',
        'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion',
        'unvigintillion', 'duovigintillion', 'trevigintillion', 'quattuorvigintillion',
        'quinquavigintillion', 'sevigintillion', 'septemvigintillion', 'octovigintillion',
        'novemvigintillion', 'vigintovigintillion', 'unvigintovigintillion', 'duovigintovigintillion',
        'trevigintovigintillion', 'quattuorvigintovigintillion', 'quinquavigintovigintillion',
        'sevigintovigintovigintillion', 'septemvigintovigintovigintillion', 'octovigintovigintovigintillion',
        'novemvigintovigintovigintillion', 'vigintovigintovigintovigintillion', 'unvigintovigintovigintovigintillion'
    ]
    
    words = [w.lower() for w in words]
    
    words = [w for w in words if len(w) > 2]
    
    words = [w for w in words if len(w) > 1]
    
    words = [w for w in words if len(w) > 0]
    
