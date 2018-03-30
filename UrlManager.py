class UrlManager():
    def url_login(self,idi):
        url='http://ygcp.njtech.edu.cn/u/'+str(idi)+'/Rscount.aspx'
        return url
    def url_userinfo(self,idi):
        url='http://ygcp.njtech.edu.cn/u/'+str(idi)+'/UserInfo.aspx'
        return url