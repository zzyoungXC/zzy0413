from urllib3.poolmanager import PoolManager
#url 下载器

#pm=PoolManager()

#result = pm.request('get','http://www.163.com')
#if result.status == 200:
#    print(result.data.decode(encoding='gbk'))

def down_html(url:str, method='get', encoding='utf-8'):
    pm = PoolManager()

    result = pm.request(method,url)
    if result.status == 200:
        print(result.data.decode(encoding=encoding))
    else:
        return None

