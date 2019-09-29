# -*- coding: utf-8 -*-

import requests, sys
from bs4 import BeautifulSoup

def getExpectEPS(codeNumber):
    url = "https://finance.naver.com/item/main.nhn?code=" + codeNumber
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    cell_strong_list = bs_obj.find_all("td", {"class": "cell_strong"}) # td 태그 중 class가 cell_strong 인 것들을 모두 찾는다
    EPS = cell_strong_list[18].text.strip().replace(",", "") # cell_strong 리스트 중 18번째 값이 EPS 이다.
    if EPS == "":
        lastEPS = getLastEPS(codeNumber)
        print("올해 예상 EPS가 없음, 작년 EPS 로 대체 : ", lastEPS)
        return lastEPS
    else:
        print("예상 EPS :",EPS)
        return EPS

def getLastEPS(codeNumber):
    url = "https://finance.naver.com/item/main.nhn?code=" + codeNumber
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    th_list = bs_obj.find(string="EPS(원)").parent.parent.parent.find_all("td") # 이상하게 find_parent는 안된다...
    lastEPS = th_list[2].text.strip().replace(",", "")

    companyName = bs_obj.find("div", {"class" : "wrap_company"}).find_next("h2").text
    # print(len(companyName) * ' ', end = '')
    print("지난해 EPS :", lastEPS)
    return lastEPS

def getFiveYearPER(codeNumber):
    url = "http://search.itooza.com/search.htm?seName=" + codeNumber
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    fiveYearSummary = bs_obj.find("table", {"summary": "5년치 주요 가치지표"}) # td 태그 중 class가 cell_strong 인 것들을 모두 찾는다
    td_list = fiveYearSummary.find_all("td")
    fiveYearPER = td_list[0].text.replace(",", "")

    companyName = bs_obj.find("span", {"class" : "name"}).text

    # print(len(companyName) * ' ', end = '')
    print("5년 평균 PER :", fiveYearPER)
    return fiveYearPER

def getReasonablePriceByPER(codeNumber):
    companyName = getCompanyName(codeNumber)
    print("[ PER을 이용한", companyName, "(", codeNumber, ")의 적정가격 구하기 ]")

    expectEPS = getExpectEPS(codeNumber)
    lastEPS = getLastEPS(codeNumber)
    fiveYearPER = getFiveYearPER(codeNumber)
    nowPrice = getNowPrice(codeNumber)

    print("적정 주가 :", round(float(lastEPS) * float(fiveYearPER)), "~", round(float(expectEPS) * float(fiveYearPER)))
    print("20% 더 싼 가격 :", round(float(lastEPS) * float(fiveYearPER) * 0.8), "~", round(float(expectEPS) * float(fiveYearPER) * 0.8))
    print("현재 가격 :", nowPrice)

def getCompanyName(codeNumber):
    url = "https://finance.naver.com/item/main.nhn?code=" + codeNumber
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    companyName = bs_obj.find("div", {"class" : "wrap_company"}).find_next("h2").text
    return companyName

def getNowPrice(codeNumber):
    url = "https://finance.naver.com/item/main.nhn?code=" + codeNumber
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    no_today = bs_obj.find("p", {"class": "no_today"}) # 태그 p, 속성값 no_today 찾기
    blind = no_today.find("span", {"class": "blind"}) # 태그 span, 속성값 blind 찾기
    nowPrice = blind.text
    return nowPrice


if len(sys.argv)-1 <= 1:
    print("python naverFinanceCrawler getExpectEPS 123456")
elif sys.argv[1] == "getExpectEPS":
    getExpectEPS(sys.argv[2])
elif sys.argv[1] == "getFiveYearPER":
    getFiveYearPER(sys.argv[2])
elif sys.argv[1] == "getLastEPS":
    getLastEPS(sys.argv[2])
elif sys.argv[1] == "getReasonablePriceByPER":
    getReasonablePriceByPER(sys.argv[2])    
else:
    print("wrong parameter!") 