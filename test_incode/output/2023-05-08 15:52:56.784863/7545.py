#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that enumerates a http request.
    def enumerate_requests(url):
        request = requests.get(url)
        request.raise_for_status()
        return request

    #A function that parses the response of a http request.
    def parse_response(request):
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = rows[0].find_all('th')
        rows = rows[1:]
        rows = [i.text for i in rows]
        rows = [i.split(',') for i in rows]
        rows = [i.split(':') for i in rows]
        rows = [i.strip() for i in rows]
        return dict(zip(header, rows))

    #A function that parses the response of a http request.
    def parse_response_json(request):
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = rows[0].find_all('th')
        rows = rows[1:]
        rows = [i.text for i in rows]
        rows = [i.split(',') for i in rows]
        rows = [i.split(':') for i in rows]
        rows = [i.strip() for i in rows]
        return dict(zip(header, rows))

    #A function that parses the response of a http request.
    def parse_response_xml(request):
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = rows[0].find_all('th')
        rows = rows[1:]
        rows = [i.text for i in rows]
        rows = [i.split(',') for i in rows]
        rows = [i.split(':') for i in rows]
        rows = [i.strip() for i in rows]
        return dict(zip(header, rows))

    #A function that parses the response of a http request.
    def parse_response_text(request):
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = rows[0].find_all('th')
        rows = rows[1:]
        rows = [i.text for i in rows]
        rows = [i.split(',') for i in rows]
        rows = [i.split(':') for i in rows]
        rows = [i.strip() for i in rows]
        return dict(zip(header, rows))

    #A function that parses the response of a http request.
    def parse_response_html(request):
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = rows[0].find_all('th')
        rows = rows[1:]
        rows = [i.text for i in rows]
        rows = [i.split(',') for i in rows]
        rows = [i.split(':') for i in rows]
        rows = [i.strip() for i in rows]
        return dict(zip(header, rows))

    #A function that parses the response of a http request.
    def parse_response_xml(request):
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = rows[0].find_all('th')
        rows = rows[1:]
        rows = [i.text for i in rows]
        rows = [i.split(',') for i in rows]
        rows = [i.split(':') for i in rows]
        rows = [i.strip() for i in rows]
        return dict(zip(header, rows))

    #A function that parses the response of a http request.
    def parse_response_text(request):
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = rows[0].find_all('th')
        rows = rows[1:]
        rows = [i.text for i in rows]
        rows = [i.split(',') for i in rows]
        rows = [i.split(':') for i in rows]
        rows = [i.strip() for i in rows]
        return dict(zip(header, rows))

    #A function that parses the response of a http request.
    def parse_response_html(request):
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = rows[0].find_all('th')
        rows = rows[1:]
        rows = [i.text for i in rows]
        rows = [i.split(',') for i in rows]
        rows = [i.split(':') for i in rows]
        rows = [i.strip() for i in rows]
        return dict(zip(header, rows))

    #A function that parses the response of a http request.
    def parse_response_xml(request):
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = rows[0].find_all('th')
        rows = rows[1:]
        rows = [i.text for i in rows]
        rows = [i.split(',') for i in rows]
        rows = [i.split(':') for i in rows]
        rows = [i.strip() for i in rows]
        return dict(zip(header, rows))

    #A function that parses the response of a http request.
    def parse_response_text(request):
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = rows[0].find_all('th')
        rows = rows[1:]
        rows = [i.text for i in rows]
        rows = [i.split(',') for i in rows]
        rows = [i.split(':') for i in rows]
        rows = [i.strip() for i in rows]
        return dict(zip(header, rows))

