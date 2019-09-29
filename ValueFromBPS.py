# -*- coding: utf-8 -*-
import sys
import pandas as pd
code_df = pd.read_html('http://search.itooza.com/search.htm?seName=000660')
PBR = code_df[1]["5년PBR"].values[0]


#print(PBR)

def getCurrentBPS(code_df_naver) :
        
    return code_df_naver[3].values[11][9]

def getFiveYearPBR(code_df_itooza) :
    return code_df_itooza[1]["5년PBR"].values[0]


def getReasonablePriceByPBR(code_df_naver, code_df_itooza) :
    BPS = getCurrentBPS(code_df_naver)
    PBR = getFiveYearPBR(code_df_itooza)
    
    print("자본기준 적정주가 : " + str(BPS * PBR))
    return BPS * PBR







if len(sys.argv) - 1 <= 1:
    print("python ValueFromBPS getCurrentBPS 123456")
elif len(sys.argv) == 3 : 
    code_df_itooza = pd.read_html('http://search.itooza.com/search.htm?seName=' + sys.argv[2])
    code_df_naver = pd.read_html('https://finance.naver.com/item/main.nhn?code=' + sys.argv[2])
    if   sys.argv[1] == "getCurrentBPS" :
        getCurrentBPS(code_df_naver)
    elif sys.argv[1] == "getFiveYearPBR" :
        getFiveYearPBR(code_df_itooza)
    elif sys.argv[1] == "getReasonablePriceByPBR" :
        getReasonablePriceByPBR(code_df_naver, code_df_itooza)
else:
    print("wrong parameter!")
