import requests
from lxml import etree
import time
import random
headers = {
    'User-Agent':':Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
start_url = 'https://maoyan.com/board/4'+'?offset={}'#分析url每个页面的url构造通用url模板
for num in range(0,91,10):
    s = random.random() * 3
    time.sleep(s)#避免网站被怕死 停顿随机停顿一下
    url = start_url.format(num)
    print(url)
    response = requests.get(url=url,headers=headers)
    html = etree.HTML(response.content.decode('utf-8'))
    dd_list = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')#返回的是一个列表
    for dd in dd_list:
        index = dd.xpath('./i/text()')[0]#排名
        title = dd.xpath('./div/div/div[1]/p[1]/a/text()')[0]#电影名称
        star = dd.xpath('./div/div/div[1]/p[2]/text()')[0].strip('\n').strip(' ').strip('\n')#主演 掉两边的空格和\n
        rtime = dd.xpath('./div/div/div[1]/p[3]/text()')[0]#上映时间
        score = dd.xpath('./div/div/div[2]/p/i[1]/text()')[0] + dd.xpath('./div/div/div[2]/p/i[2]/text()')[0]

        print(index)
        print(title)
        print(star)
        print(rtime)
        print(score)
