import json
from bs4 import BeautifulSoup
import requests

with open("output.json","r",encoding="utf8") as f:
    file = json.load(f)

for para1 in range(8):
    res = requests.get(file[para1]["sum_title_url"])
    soup = BeautifulSoup(res.text,"html.parser")
    content_all = soup.find("div",class_="indent").find_all("p")
    with open (f"sum_{file[para1]['category']}_{file[para1]['sum_title'][:4]}","w",encoding="utf8") as fp:
        for title in content_all:
          json.dump(title.text,fp,ensure_ascii=False)
          fp.write("\n")

    spot_con = file[para1]["spotlist"]
    
    for spotlight in range(3):
        res = requests.get(spot_con[spotlight]["url"])
        soup = BeautifulSoup(res.text,"html.parser")
        content_all = soup.find("div",class_="indent").find_all("p")
        with open (f"spot_{file[para1]['category']}_{spot_con[spotlight]['title'][:4]}","w",encoding="utf8") as fp:
          for spot in content_all:
            json.dump(spot.text,fp,ensure_ascii=False)
            fp.write("\n")