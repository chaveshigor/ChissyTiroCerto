import requests
from bs4 import BeautifulSoup

def write(string):
    string = str(string)
    file = open('teste.html', 'w')
    file.writelines(string)

class League:

    def __init__(self, leagueUrl):
        self.leagueUrl = leagueUrl
        self.getTeams()

    def getTeams(self):
        url = self.leagueUrl
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            # noqa
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Dnt": "1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            # noqa
        }
        page = requests.get(url, headers=headers)
        info = BeautifulSoup(page.content, 'html.parser')
        
        allTables = info.find_all('table')
        championshipTable = allTables[-2]

        write(championshipTable)