import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# メールアドレスとパスワードの指定
USER = "tomoakihori5"
PASS = "kmkzmv2600"

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "userid": USER,
    "password": PASS,
    "btnNormal01Large maB10": "ログイン"
}
action = "https://www.smbc-card.com/memapi/jaxrs/xt_login/agree/v1"
# url_login="https://www.smbc-card.com/memapi/jaxrs/xt_login/agree/v1"
# action
url_login = "https://www.smbc-card.com/mem/index.jsp?"
res = session.post(url_login, data=login_info)
res.raise_for_status()  # エラーならここで例外を発生させる

print(res.text)

# だめだこれは
