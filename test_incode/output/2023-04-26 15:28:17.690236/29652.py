#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes all ports and converts fruits. """    
    while True:
        ports = range(1,5)
        fruits = [1,2,3,4,5,6,7,8,9,10]
        fruits_multiply = []
        for port in ports:
            fruits_multiply.append(fruits[port-1]*fruits[port])
        fruits_multiply = sum(fruits_multiply)
        print(fruits_multiply)
        time.sleep(1)
</code>
<|/ a dscore=0 |>
<| c |>
Thanks for your help, however I still get the same error when I run it
<|/ c |>
<| c |>
I added the full code to the original post
<|/ c |>
<| c |>
I added the full code to the original post
<|/ c |>
<| c |>
I added the full code to the original post
<|/ c |>
<| c |>
I added the full code to the original post
<|/ c |>
<| a dscore=0 |>
The code below should work. 
<code>
#!/usr/bin/python
