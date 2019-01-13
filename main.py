import requests
import json
from bs4 import BeautifulSoup

def crawler(character):
        if character == "lucky-chloe":
            url = "http://rbnorway.org/" + character + "-t7-frames/"
            websitecode = requests.get(url)
            text = websitecode.text
            soup = BeautifulSoup(text, "html.parser")

            rows = soup.find_all("tr")
            alltd = soup.find_all("td")

            headers = {}
            thead = soup.find("tr")
            if thead:
                thead = thead.find_all("th")
                for i in range(8):
                    headers[i] = thead[i].text.strip()
            data = []
            tdindex = 0
            rows.pop()
            for row in rows:
                items = {}
                for index in headers:
                    try:
                        items[headers[index]] = alltd[tdindex].text
                        tdindex = tdindex + 1
                    except IndexError:
                        break

                data.append(items)
            return json.dumps(data, indent=4)

        elif character == "marduk":
            url = "http://rbnorway.org/" + character + "-t7-frames/"
            websitecode = requests.get(url)
            text = websitecode.text
            soup = BeautifulSoup(text, "html.parser")

            rows = soup.find_all("tr")
            alltd = soup.find_all("td")

            headers = {}
            thead = soup.find("tr")
            if thead:
                thead = thead.find_all("td")
                for i in range(8):
                    headers[i] = thead[i].text.strip()
            data = []
            tdindex = 0
            for row in rows:
                cells = row.find_all("td")
                if headers[1] == cells[1].text:
                    continue
                else:
                    if tdindex >= 1048:
                        break
                    else:
                        items = {}
                        for index in headers:
                            try:
                                items[headers[index]] = alltd[tdindex].text
                                tdindex = tdindex + 1
                            except IndexError:
                                break
                        data.append(items)
            return json.dumps(data, indent=4)

        else:
            url = "http://rbnorway.org/" + character + "-t7-frames/"
            websitecode = requests.get(url)
            text = websitecode.text
            soup = BeautifulSoup(text, "html.parser")

            rows = soup.find_all("tr")

            headers = {}
            thead = soup.find("tr")
            if thead:
                thead = thead.find_all("td")
                for i in range(8):
                    headers[i] = thead[i].text.strip()
            data = []
            for row in rows:
                cells = row.find_all("td")
                if headers[1] == cells[1].text:
                    continue
                else:
                    items = {}
                    for index in headers:
                        items[headers[index]] = cells[index].text

                    data.append(items)
            return json.dumps(data, indent=4)


characters = ["akuma", "alisa", "anna", "armor-king", "asuka", "bob", "bryan", "claudio", "devil-jin", "dragunov", "eddy", "eliza", "feng", "geese", "gigas", "heihachi", "hwoarang", "jack7", "jin", "josie", "katarina", "kazumi", "kazuya", "king", "kuma", "lars", "lei", "law", "lee", "leo", "lili", "lucky-chloe", "marduk", "master-raven", "miguel", "nina", "noctis", "paul", "shaheen", "steve", "xiaoyu", "yoshimitsu"]
for char in characters:
    f = open(char + '.json', 'w')
    print(crawler(char), file=f)
