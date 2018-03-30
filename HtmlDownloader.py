import requests
from bs4 import BeautifulSoup
from UrlManager import UrlManager

class HtmlDownloader(object):
    
    def download(self,url,idi,url_login,url_userinfo):

        user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        header={'Referer': 'http://ygcp.njtech.edu.cn/Index.aspx','User-Agent':user_agent}
        s=requests.Session()
        postdata={
            'LoginUserName':idi,
            'LoginPassword':'111111',
            'AutoLogin':'true',
            'login':'登  录'
        }
        s.post(url,data=postdata,headers=header)
        f=s.get(url_login,headers=header)#我的成绩页面
        i=s.get(url_userinfo,headers=header)#个人信息页面
        # print (f.text)
        return f.text,i.text
        

def main():
    idi=1405150114
    urlmanager=UrlManager()
    pageur=urlmanager.url_login(idi)
    infourl=urlmanager.url_userinfo(idi)
    htmldownloader=HtmlDownloader()
    htmldownloader.download('http://ygcp.njtech.edu.cn/User/LoginInSampleAction.aspx',
    idi,pageur,infourl
    )


if __name__ == '__main__':
    main()
