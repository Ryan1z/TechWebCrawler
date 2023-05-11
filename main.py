import requests
from bs4 import BeautifulSoup
import json

url = "https://technews.tw/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

paragraph = soup.find("ul", class_="screen")

outputList = []

for para1 in paragraph.find_all("li", class_="block2014"):
    outputDict = {}
    outputDict['category'] = para1.find("div", class_="cat01").text
    outputDict['sum_title'] = para1.find("h3").text
    outputDict['sum_title_url'] = para1.find("a").get("href")
    outputDict['spotlist'] = []
    
    for spot in para1.find_all("li", class_="spotlist"):
        spot_info = {}
        spot_info['title'] = spot.find("a").text
        spot_info['url'] = spot.find("a").get("href")
        outputDict['spotlist'].append(spot_info)

    outputList.append(outputDict)

with open('output.json', 'w', encoding='utf-8') as fp:
    json.dump(outputList, fp, ensure_ascii=False, indent=4)
