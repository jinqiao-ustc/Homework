import requests
from lxml import etree
from urllib import request
import os
import re
import threading
from queue import Queue

#自定义类
class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'Referer': 'https://movie.douban.com/'
    }

    #初始化
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    #获得表情包相关信息
    def parse_page(self,url):
        response = requests.get(url,headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        for img in imgs:
            #图片地址
            img_url = img.get('data-original')
            #图片名字
            alt = img.get('alt')
            #替换掉名字里面的特殊字符
            alt = re.sub(r'[\?？\.，。！!\*]','',alt)
            #获取图片的后缀名（.gif .jpg）
            suffix = os.path.splitext(img_url)[1]
            #保存的时候完整的图片名字
            filename = alt + suffix
            self.img_queue.put((img_url,filename))


#自定义类，多线程下载
class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            request.urlretrieve(img_url, '/Users/jin/PycharmProjects/Homework/level5/data/' + filename)
            print("已下载完一张图片")


#main
def main():
    page_queue = Queue(1000)
    img_queue = Queue(100)

    for x in range(1,100):
        url = 'http://www.doutula.com/photo/list/?page=%d'%x
        page_queue.put(url)

    for x in range(10):
        t = Producer(page_queue,img_queue)
        t.start()

    for x in range(10):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()