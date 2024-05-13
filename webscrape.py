from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.dota2.com/heroes"
params = {}

response = requests.get(url=url, params=params)

soup  = BeautifulSoup(response.text, "html.parser")

hero_links = soup.find_all("a", {"class":"_7szOnSgHiQLEyU0_owKBB"})

print(response.text)

for hero in hero_links:
  print("test")
  print(hero.style)