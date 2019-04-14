class UrlManager(object):
    #two set ,存储待爬的和已爬的
    def __init__(self):
        self.new_url=set()
        self.old_url=set()
    #把新的url地址添加到待爬集合中
    def add_url(self,url):
        if url not in self.new_url and url not in self.old_url:
            self.new_url.add(url)
    #支持添加url序列
    def add_urls(self,urls):
        for url in urls:
            self.add_url(url)
    #获取待爬url地址
    def get_url(self):
        #待爬集合随机返回url地址
        url=self.new_url.pop()
        #此地址添加到已爬的url地址中
        self.old_url.add(url)
        return url
    #判断当前url中是否还有数据
    def has_url(self,urls):
        return len(self.new_url)>0

if __name__== '__main__':
    um=UrlManager()
    l=['aa','aasda','fasd']
    um.add_url(l)
    print(um.new_url,um.old_url)
    url=um.get_url()
    print(um.new_url,um.old_url)
    print(um.has_url())