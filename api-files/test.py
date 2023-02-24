import whois
from urllib.parse import urlparse
from datetime import datetime
import urllib.request as urllib2
from bs4 import BeautifulSoup
import requests
import similarweb

# def simweb(ip):
#     try:
#         domain = whois.whois(urlparse(ip).netloc)
#         domain = domain.domain
#         url = "https://www.similarweb.com/website/"+domain+"/#overview"
#         hdr = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0(HTTP_USER_AGENT)"}
#         req = requests.get(url,headers=hdr)
#         soup = BeautifulSoup(req.text, 'html.parser')
#         print(soup)
#         # urllib2.urlopen(req)  # .find("REACH")['RANK']
#         # if (int(rank) < 100000):
#             # return 1
#         # elif (int(rank) > 100000):
#             # return 0
#     except Exception as e:
#         print(e)
#         return -1

def contains_dash(ip):
    if('https' in ip):
        start = 7
    elif('http' in ip):
        start = 6
    pos = ip.find('/',start)
    if(ip.find('-') < pos):
        return -1
    else:
        return 1


print(contains_dash('https://stackoverflow.com/questions/41620369/how-to-get-ssl-certificate-details-using-python'))
# domain = whois.whois(urlparse('https://github.com/polybar/polybar/wiki/Module:-xworkspaces').netloc)
# print(domain)
