# Baidupic
scrapy框架爬取百度图片，使用scrapyd可以用json api调用爬虫，还可以传入keywords 和 page来指定爬取的内容，图片地址保存在本地.json文件供web框架使用,在piplines.py里可以改变储存方式，比如储存在数据库，用pymsql或者pymango，进入项目目录命令行输入命令scrapyd，向地址localhost:6800/schedule.json发送post请求，参数urlencode，类似这样http://localhost:6800/schedule.json?project=baidupic&spider=baidupicspider&keywords=美女&page=10 ，page默认10，可以不传，其他三个必传，端口可以在scrapy.cfg配置
