#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A program that opens a http request.
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    req.add_header('Accept-Encoding', 'gzip, deflate')
    req.add_header('Accept-Language', 'en-US,en;q=0.8')
    req.add_header('Connection', 'keep-alive')
    req.add_header('Host', 'snirps.ddns.net')
    req.add_header('Referer', 'http://snirps.ddns.net')
    req.add_header('X-Requested-With', 'XMLHttpRequest')
    req.add_header('X-CSRF-Token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.Y2tjbVN0Y2VydmljZSIsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLCJpYXQiOjE0NjQ4NzUsImV4cCI6MTU2NzQxNzE1NywiZXhwIjoxNjE1NjM5MDIyLC

