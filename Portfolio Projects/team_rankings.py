import requests
from bs4 import BeautifulSoup

supported_inputs = ["NBA", "MLB", "NFL", "MLS"]

MLB_URL = ""
NBA_URL = "https://stats.nba.com/standings/"
NFL_URL = ""
MLS_URL = ""

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 "
                         "(KHTML, like Gecko) Version/13.0.4 Safari/605.1.15"}

def get_rank():
    #if input == "NBA":
    page = requests.get(NBA_URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    team_rank = soup.find(class_="team_nowrap").get_text()

    print(team_rank)

get_rank()