
# import package เข้ามา
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup


def CheckGOLDprice ():

    url = 'https://www.goldtraders.or.th/'
    webopen = req(url) #เปิดเว็บโดยไม่เปิด web browser
    page_html = webopen.read() #code html ไปใช้งานต่อ
    webopen.close()
    data = soup(page_html,'html.parser') #แปลงเป็น soup
    allclass = ['DetailPlace_uc_goldprices1_lblBLSell','DetailPlace_uc_goldprices1_lblBLBuy','DetailPlace_uc_goldprices1_lblOMSell','DetailPlace_uc_goldprices1_lblOMBuy']
    
    allprice = []
    for al in allclass:
        rawdata = data.find_all('span',{'id':al})
        #print(rawdata)
        allprice.append(float(rawdata[0].text.replace(',','')))
    print(allprice)
    header=['gold price-sell','gold price-buy', 'gold price general-sell','gold price general-buy']
    result = {}
    for h,p in zip(header,allprice):
        result[h] = p
    #print (result)
    return result

price = CheckGOLDprice()
print(price)
    
 