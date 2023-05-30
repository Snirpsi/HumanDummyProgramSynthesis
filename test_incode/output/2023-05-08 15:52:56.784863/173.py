#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that opens a http request.
    def httpGet(url):
        try:
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            return response.read()
        except urllib.error.URLError as e:
            print(e)
            return None
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.find('table', attrs={'class': 'table table-striped table-hover'})
        rows = table.find_all('tr')
        header = []
        for row in rows:
            cells = row.find_all('td')
            header.append(cells[0].text)
        return header
    #A function that parses the response from the http request.
    def httpGetResponse(response):
        soup = BeautifulSoup(response, 'html.parser')
        table = soup.

