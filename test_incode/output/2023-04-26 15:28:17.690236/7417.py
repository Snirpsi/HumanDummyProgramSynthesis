#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words or removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words|numbers>' % sys.argv[0])
        sys.exit()
    
    words = []
    numbers = []
    
    for arg in sys.argv[1:]:
        if arg == 'words':
            words = sys.argv[2:]
        elif arg == 'numbers':
            numbers = sys.argv[2:]
        else:
            print('Unknown argument %s' % arg)
            sys.exit()
    
    words.sort()
    numbers.sort()
    
    for word in words:
        print('%s %s' % (word, numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (words[-1], numbers.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[-1], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(words) > 0:
        print('%s %s' % (words[0], numbers.pop(0)))
    
    if len(numbers) > 0:
        print('%s %s' % (numbers[0], words.pop(0)))
    
    if len(