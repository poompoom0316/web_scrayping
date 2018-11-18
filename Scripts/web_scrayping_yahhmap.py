# coding: UTF-8
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import urllib.request, urllib.error
import pandas as pd
import numpy as np

# セッションを開始
url0 ='http://www.karaokemanekineko.jp/'
url = 'http://www.karaokemanekineko.jp/shop/kinki-area/hyougo/'
res = urllib.request.urlopen(url)
soup = BeautifulSoup(res, "lxml")
soup.find_all("a", class_="shop-name").get("href")

# kinki-areaの全店舗のurlを取得する
urls = [i.get("href") for i in soup.select('a[href^="/shop/kinki-area/"]')]

# yahoo地図の緯度経度を取得する
df_urls = pd.DataFrame(None, index=urls, columns=['lat', 'lon'])

for urli in urls:
    resi = urllib.request.urlopen(url0+urli)
    soupi = BeautifulSoup(resi, "lxml")
    # 中身の取り出し
    lat = soupi.find(id="map_canvas").contents[3].get('src').split('?lat=')[1].split('&lon=')[0]
    lon = soupi.find(id="map_canvas").contents[3].get('src').split('&lon=')[1].split('&pluginid')[0]
    df_urls.loc[urli, :] = np.array([lat, lon]).astype(float)

