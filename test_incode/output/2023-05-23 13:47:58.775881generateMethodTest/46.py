#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that stores a http request.
    def http_request(url, method, body):
        req = urllib.request.Request(url, data=body)
        req.add_header('Content-Type', 'application/json')
        req.add_header('Accept', 'application/json')
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')
        req.add_header('Accept-Encoding', 'gzip, deflate')
        req.add_header('Accept-Language', 'en-US,en;q=0.8')
        req.add_header('Connection', 'keep-alive')
        req.add_header('Host', url)
        req.add_header('Referer', url)
        req.add_header('X-Requested-With', 'XMLHttpRequest')
        req.add_header('X-CSRFToken', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3NlcnZpY2UuY29tLmNvbS9pZCI6IjIwMTQ0NzIyMzU0NjY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNzY2NzkzNz