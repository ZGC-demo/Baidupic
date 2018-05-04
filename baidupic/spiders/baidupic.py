import scrapy
import json
from ..items import BaidupicItem


class BaidupicSpider(scrapy.Spider):
    name = 'baidupicspider'
    allowed_domains = ['image.baidu.com']
    pn = 0

    def __init__(self, keywords=None, page=None, *args, **kwargs):
        super(BaidupicSpider, self).__init__(*args, **kwargs)
        self.init_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%s&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=%s&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&rn=30&gsm=&1525406929428=&pn=0' % (keywords, keywords)
        self.start_urls = [self.init_url + str(30*x) for x in range(1, int(page))]

    def parse(self, response):
        data = json.loads(response.text)["data"]
        for each in data:
            if not each.__contains__('thumbURL'):
                continue
            item = BaidupicItem(url=each['thumbURL'])
            yield item



