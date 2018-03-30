from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from UrlManager import UrlManager
class Spider(object):
    def __init__(self):
        self.manager=UrlManager()
        self.downloader=HtmlDownloader()
        self.paser=HtmlParser()
    def crawl(self,idi):
        rootloginurl='http://ygcp.njtech.edu.cn/User/LoginInSampleAction.aspx'
        pageurl=self.manager.url_login(idi)
        infourl=self.manager.url_userinfo(idi)
        htmlf,htmli=self.downloader.download(rootloginurl,idi,pageurl,infourl)
        xuehao,xingming,changpao,chenpao=self.paser.parser(infourl,pageurl,htmli,htmlf)
        print("学号："+xuehao[0],
                "姓名:"+xingming[0],
                changpao,chenpao)
def main():
    start=input('输入起始学号：')
    end=input('结束学号：')
    i =int(start)
    for i in range(int(start),int(end)):
        spider_man=Spider()
        spider_man.crawl(i)
        i+=i

if __name__ == '__main__':
    main()