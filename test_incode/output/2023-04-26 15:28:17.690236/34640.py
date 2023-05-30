#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a list of words and removes a port. """    
    words = removePort(['i', 'am', 'a', 'test', 'port'])
    print(words)
</code>
<|/ a dscore=0 |>
<| c |>
Thank you very much! This was very helpful!
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>
<| a tags=python,python-3.x |>
<code>
def removePort(words):
    words = [w for w in words if not w.startswith('