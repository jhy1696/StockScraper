# -*- coding: utf-8 -*-

import requests, sys
from bs4 import BeautifulSoup

def getEPS(codeNumber):
    url = "https://finance.naver.com/item/main.nhn?code=" + codeNumber
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    cell_strong_list = bs_obj.find_all("td", {"class": "cell_strong"}) # td 태그 중 class가 cell_strong 인 것들을 모두 찾는다
    EPS = cell_strong_list[18].text.strip().replace(",", "") # cell_strong 리스트 중 18번째 값이 EPS 이다.

    companyName = bs_obj.find("div", {"class" : "wrap_company"}).find_next("h2").text
    print(companyName)
    print("EPS")
    print(EPS)
    return EPS

if (sys.argv[1] == "getEPS"):
    getEPS(sys.argv[2])