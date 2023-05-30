#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a port. """    
    port = int(sys.argv[1])
    httpd = make_server('', port, MyHandler)
    print('Serving on port {}'.format(port))
    httpd.serve_forever()
</code>
<|/ a tags=python,webserver,sockets,python-3.x |>
<| c |>
This answer does not provide an answer to the question. Once you have sufficient [reputation](https://stackoverflow.com/help/whats-reputation) you will be able to [comment on any post](https://stackoverflow.com/help/privileges/comment); instead, [provide answers that don't require clarification from the asker](https://meta.stackexchange.com/questions/214173/why-do-i-need-50-reputation-to-comment-what-can-i-do-instead). - [From Review](/review/low-quality-posts/27709443)
<|/ c |>
<| c |>
Thanks for your comment. I will try to improve the answer as soon as possible.
<|/ c |>
<| c |>
I added a comment to the answer.
<|/ c |>
<| c |>
Thanks for your answer. Your answer was very helpful.
<|/ c |>
<| c |>
No problem. Glad I could help.
<|/ c |>