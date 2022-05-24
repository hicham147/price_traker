from bs4 import BeautifulSoup
from requests_html import HTMLSession

def get_ihreb_data(url):
    s = HTMLSession()
    headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    r = s.get(url,headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    try:
        title = soup.find("div",{"class":"product-summary-title"}).text.strip()
    except:
        title = ''
    price = soup.find("section", {"id": "product-price"}).find("div", {"id": "price"}).text.replace("SAR", "").replace("DA", "").strip().replace(',','')
    price = float(price)
    return title,price


def get_niceone_data(url):
    s = HTMLSession()
    headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    r = s.get(url,headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find("h1",{"class":"title"}).text.strip()
    price = float(soup.find("h3",{"class":"preReductionPrice mb-2"}).text.replace("SAR","").replace("ريال","").strip())
    return title,price


def get_amazon_price(url):
    s = HTMLSession()
    headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    r = s.get(url,headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find("div",{"id":"titleSection"}).text.strip()
    try:
        price = float(soup.find("div", {"id": "corePrice_feature_div"}).find("span", {"class": "a-offscreen"}).text.replace("ريال",""))
    except:
        price = float(soup.find("div", {"id": "corePrice_feature_div"}).find("span", {"class": "a-offscreen"}).text.replace("SAR", ""))
    return title,price




def get_xcite_price(url):
    s = HTMLSession()
    headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
    r = s.get(url,headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    title = soup.find("div",{"class":"product-name"}).find("h1").text.strip()
    price = soup.find("div",{"class":"you-pay-box"}).find("span").text.replace("SR","").replace(",","").replace("\u200f","").strip()
    price = float(price)
    return (title,price)