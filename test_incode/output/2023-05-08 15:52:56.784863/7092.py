#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A function that enumerates a http request.
    def http_request(url):
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        html = response.read()
        return html
    #A function that parses the html and returns the data.
    def html_parser(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_2(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_3(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_4(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_5(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_6(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_7(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_8(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_9(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_10(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_11(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_12(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the html and returns the data.
    def html_parser_13(html):
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        rows = table.find_all('tr')
        header = []
        for row in rows:
            header.append(row.find_all('th')[0].text)
        data = []
        for row in rows:
            data.append(row.find_all('td')[0].text)
        return data
    #A function that parses the 

