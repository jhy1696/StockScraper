# -*- coding: utf-8 -*-
import requests, sys
import pandas as pd
from bs4 import BeautifulSoup

import search   #user module

def getReasonablePriceByPBR(codeNumber) :
    BPS = search.getCurrentBPS(codeNumber)
    PBR = search.getFiveYearPBR(codeNumber)
    
    companyName = search.getCompanyName(codeNumber)
    print("[ PBR을 이용한", companyName, "(", codeNumber, ")의 적정가격 구하기 ]")
    print("자본기준 적정주가 : " + str(round(float(BPS * PBR))))
    return BPS * PBR

def getReasonablePriceByPER(codeNumber):
    companyName = search.getCompanyName(codeNumber)
    print("[ PER을 이용한", companyName, "(", codeNumber, ")의 적정가격 구하기 ]")

    expectEPS = search.getExpectEPS(codeNumber)
    lastEPS = search.getLastEPS(codeNumber)
    fiveYearPER = search.getFiveYearPER(codeNumber)
    nowPrice = search.getNowPrice(codeNumber)

    print("적정 주가 :", round(float(lastEPS) * float(fiveYearPER)), "~", round(float(expectEPS) * float(fiveYearPER)))
    print("20% 더 싼 가격 :", round(float(lastEPS) * float(fiveYearPER) * 0.8), "~", round(float(expectEPS) * float(fiveYearPER) * 0.8))
    print("현재 가격 :", nowPrice)