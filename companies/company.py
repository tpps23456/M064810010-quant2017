import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    message = """請在網址列上選擇要看的公司名單：<br/>
    /nasdaq ==> nasdaq 的公司名單<br/>
    /nyse ==> nyse 的公司名單<br/>
    /amex ==> amex 的公司名單<br/>
    """
    return message

@app.route('/nyse')
def nyse():
    df = pd.read_csv("nyse_companylist.csv", encoding="utf-8", header=0)
    df.sort_index(ascending=True)
    return df.to_html()

@app.route('/nyse/<symbol>')
def nyse_company(symbol):
    df = pd.read_csv("nyse_companylist.csv",encoding="utf-8", header=0)
    df.sort_index(ascending=True)
    match = df.loc[df['Symbol'] == symbol.upper()]
    return match.to_html()

@app.route('/nasdaq')
def nasdaq():
    df = pd.read_csv("nasdaq_companylist.csv", encoding="utf-8", header=0)
    df.sort_index(ascending=True)
    return df.to_html()

@app.route('/nasdaq/<symbol>')
def nasdaq_company(symbol):
    df = pd.read_csv("nasdaq_companylist.csv",encoding="utf-8", header=0)
    df.sort_index(ascending=True)
    match = df.loc[df['Symbol'] == symbol.upper()]
    return match.to_html()

@app.route('/amex')
def amex():
    df = pd.read_csv("amex_companylist.csv", encoding="utf-8", header=0)
    df.sort_index(ascending=True)
    return df.to_html()

@app.route('/amex/<symbol>')
def amex_company(symbol):
    df = pd.read_csv("amex_companylist.csv",encoding="utf-8", header=0)
    df.sort_index(ascending=True)
    match = df.loc[df['Symbol'] == symbol.upper()]
    return match.to_html()


if __name__=="__main__":
    app.run()