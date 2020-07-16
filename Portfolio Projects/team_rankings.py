import doc as doc
import requests
from bs4 import BeautifulSoup
import lxml.html as lh  # Used for parsing html tables
import pandas as pd  # Used for storing the gathered data in a Pandas Dataframe

supported_inputs = ["NBA", "MLB", "NFL", "MLS"]

MLB_URL = "https://www.espn.com/mlb/standings"
NBA_URL = "https://stats.nba.com/standings/"
NFL_URL = "https://www.nfl.com/standings/league/2020/reg/"
MLS_URL = "https://www.mlssoccer.com/standings"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 "
                         "(KHTML, like Gecko) Version/13.0.4 Safari/605.1.15"}


def get_rank_nba():
    # if input == "NBA":
    page = requests.get(NBA_URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    tr_elements = doc.xpath("//tr")

    col = []
    i = 0

    for t in tr_elements():
        i += 1
        name = t.text_content()
        print("d:'%s'" % (i, name))
        col.append((name, []))

    team_rank = soup.find(class_="team_nowrap").get_text()

    print(team_rank)


def get_rank_mls():
    # if input == "MLS":
    page = requests.get(MLB_URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    tr_elements = doc.xpath("//tr")

    col = []
    i = 0

    for t in tr_elements():
        i += 1
        name = t.text_content()
        print("d:'%s'" % (i, name))
        col.append((name, []))

    #team_rank = soup.find(class_="hide-column table-data-position").get_text()

    #(printteam_rank)

get_rank_mls()