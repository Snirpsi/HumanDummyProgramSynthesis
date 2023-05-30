#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores numbers or stores words. """    
    while True:
        line = input('Enter a number: ')
        try:
            number = int(line)
        except ValueError:
            print('That is not a number')
            continue
        else:
            break
    while True:
        line = input('Enter a word: ')
        try:
            word = line.split()
        except ValueError:
            print('That is not a word')
            continue
        else:
            break
    print('The number was', number)
    print('The word was', word)
</code>
<|/ a |>
<| c |>
Thank you very much! I didn't know about this kind of loops.
<|/ c |>
<| c |>
No problem! Glad I could help!
<|/ c |>
<| a dscore=0 tags=python,loops |>
<code>
while True:
    line = input('Enter a number: ')
    try:
        number = int(line)
    except ValueError:
        print('That is not a number')
        continue
    else:
        break
while True:
    line = input('Enter a word: ')
    try:
        word = line.split()
    except ValueError:
        print('That is not a word')
        continue
    else:
        break
print('The number was', number)
print('The word was', word)
</code>
<|/ a |>
<| c |>
Thank you very much! I didn't know about this kind of loops.
<|/ c |>
<| a dscore=0 tags=python,loops |>
<code>
while True:
    line = input('Enter a number: ')
    try:
        number = int(line)
    except ValueError:
        print('That is not a number')
        continue
    else:
        break
while True:
    line = input('Enter a word: ')
    try:
        word = line.split()
    except ValueError:
        print('That is not a word')
        continue
    else:
        break
print('The number was', number)
print('The word was', word)
</code>
<|/ a |>
<| c |>
Thank you very much! I didn't know about this kind of loops.
<|/ c |>