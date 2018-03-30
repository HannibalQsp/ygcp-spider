from bs4 import BeautifulSoup
import re
import urllib
from HtmlDownloader import HtmlDownloader
from UrlManager import UrlManager

class HtmlParser(object):
    def parser(self,info_url,page_url,info_cont,page_cont):
        soup1=BeautifulSoup(info_cont,'lxml')
        soup2=BeautifulSoup(page_cont,'html.parser')
        # print(page_cont)
        # print (soup2)
        idnum=self.get_id(info_url,soup1)
        name=self.get_name(info_url,soup1)
        changp=self.get_changp(page_url,soup2)
        chenp=self.get_chenp(page_url,soup2)
        # print ('xuehao:'+idnum[0],'xingming:'+name[0],changp,chenp)
        return idnum,name,changp,chenp
    def get_id(self,info_url,soup):
        idi=[]
        idtag=soup.find('label',attrs={'name':'UserName'})
        idi.append(idtag.get_text())
        return idi
    def get_name(self,info_url,soup):
        name=[]
        namen=soup.find('label',attrs={'name':'NickName'})
        name.append(namen.get_text())
        return name
    def get_changp(self,page_url,soup):
        p=[]
        changp=soup.select('td')[0]
        p.append(changp.get_text())
        # print(soup)
        # print(p[0])
        return p[0]
    def get_chenp(self,page_url,soup):
        p=[]
        chenp=soup.select('td')[2]
        p.append(chenp.get_text())
        # print(soup)
        # print(p[0])
        return p[0]
def main():
    idi=1405150114
    urlmanager=UrlManager()
    pageurl=urlmanager.url_login(idi)
    infourl=urlmanager.url_userinfo(idi)
    htmldownloader=HtmlDownloader()
    htmlf,htmli=htmldownloader.download('http://ygcp.njtech.edu.cn/User/LoginInSampleAction.aspx',
    idi,pageurl,infourl)
    parse=HtmlParser()
    parse.parser(infourl,pageurl,htmli,htmlf)

if __name__ == '__main__':
    main()