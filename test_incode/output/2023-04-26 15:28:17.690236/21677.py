#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes user input or removes all ports. """    
    ports = input("Enter ports separated by commas: ")
    ports = ports.split(",")
    ports = [int(p) for p in ports]
    ports = [p for p in ports if p > 0]
    ports = [p for p in ports if p < 65535]
    ports = list(set(ports))
    ports.sort()
    print(ports)
</code>
<|/ a dscore=0 |>
<| c |>
This is not an answer to the question. OP asked for ports separated by commas. Your solution will remove all ports, not just those that are greater than 0.
<|/ c |>
<| c |>
I agree with you, however I thought it was a good idea to show him how to do it. And I did it anyway because he asked for ports separated by commas. Anyway I edited my answer to show how he can do it.
<|/ c |>
<| c |>
I understand your point, but I still think your answer should have been a comment. Your solution doesn't answer the question at all. OP asked for ports separated by commas. Your solution will remove all ports, not just those that are greater than 0.
<|/ c |>
<| c |>
I agree with you, but I thought it was a good idea to show him how to do it. And I did it anyway because he asked for ports separated by commas. Anyway I edited my answer to show how he can do it.
<|/ c |>
<| c |>
I understand your point, but I still think your answer should have been a comment. Your solution doesn't answer the question at all. OP asked for ports separated by commas. Your solution will remove all ports, not just those that are greater than 0.
<|/ c |>
<| a tags=python |>
<code>
ports = input("Enter ports separated by commas: ")
ports = ports.split(",")
ports = [int(p) for p in ports]
ports = [p for p in ports if p > 0]
ports = list(set(ports))
ports.sort()
print(ports)
</code>
<|/ a dscore=0 |>
<| c |>
Please add some explanation to your answer. Code only answers are discouraged.
<|/ c |>
<| a tags=python |>
<code>
ports = input("Enter ports separated by commas: ")
ports = ports.split(",")
ports = [int(p) for p in ports]
ports = [p for p in ports if p > 0]
ports = list(set(ports))
port