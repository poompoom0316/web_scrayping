# coding: UTF-8
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests

if __name__ == '__main__':
    # URL関連
    url = "https://www.smbc-card.com/mem/index.jsp"
    login = "tomoakihori5"
    password = "kmkzmv2600"

    # ヘッドレスモードの設定。
    # True => ブラウザを描写しない。
    # False => ブラウザを描写する。
    options = Options()
    options.set_headless(True)

    # Chromeを起動
    driver = webdriver.Firefox()
    driver.get(url=url)
    url2 = 'https://www.smbc-card.com/memx/web_meisai/top/index.html#info2'
    url3 = "https://www.smbc-card.com/memx/authori/shokai/index.html"

    # ログインページを開く
    driver.get(url)

    # ログオン処理
    # ユーザー名入力
    driver.find_elements_by_name("userid")[1].send_keys(login)
    driver.find_elements_by_name("password")[1].send_keys(password)
    driver.find_elements_by_class_name('btnNormal01Large')[1].send_keys(Keys.ENTER)

    # ブラウザの描写が完了させるためにsleep
    sleep(10)

    # soupオブジェクトを作成
    html = requests.get(url=url2)
    soup = BeautifulSoup(driver.page_source, "lxml")
    # soup2 = BeautifulSoup(html)
    # ログイン後のトップページのソースを表示
    print(soup)

    # 他のページ
    driver.find_elements_by_class_name('btn_md_menu_01_02')
    driver.find_elements_by_class_name('btn_md_menu_01_01')

    for i, line in enumerate(soup.prettify().split('\n')):
        if (i > 300) & (i < 430):
            print(i, len(line), line)


    driver.get(url3)

    # cookieの受け渡し
    session = requests.session()
    for cookie in driver.get_cookies():
        session.cookies.set(cookie["name"], cookie["value"])
    # requestsで取得
    response = session.get(url3)
    print(response.text)