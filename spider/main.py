from spider import *


class Spider():
    def __init__(self):
        self.baseUrl = 'https://www.shicimingju.com'
        self.choices = {'作者': 0, '标题': 1, '诗句': 2, '句首': 3, '句尾': 4, '古籍': 5, '成语': 6}
        self.choice = ''
        self.choiceId = 0
        self.keys = ''
        self.datas = ''
        self.dirs = ''
        self.fpath = ''

    #搜索
    def search_keys(self):
        self.datas = ''
        print('搜索类型：作者，标题，诗句，句首，句尾，古籍，成语')
        self.choice = input('输入搜索类型：')
        self.choiceId = self.choices[self.choice]
        self.keys = input('输入搜索关键词：')
        url = get_url(self.baseUrl, self.choiceId, self.keys)

        if self.choiceId == 0:
            status = True
            nextUrl = url
            while (nextUrl != self.baseUrl):
                print('正在爬取 ' + nextUrl + '\n')
                html = get_html(nextUrl)
                data, nextUrl, status = get_data_zuozhe(html, status)
                self.datas += data
                nextUrl = self.baseUrl + nextUrl
        elif self.choiceId >= 1 and self.choiceId <= 4:
            print('正在爬取 ' + url + '\n')
            html = get_html(url)
            data = get_data_part(html)
            self.datas += data
        elif self.choiceId == 5:
            print('正在爬取 ' + url + '\n')
            html = get_html(url)
            data = get_data_book(self.baseUrl, html)
            self.datas += data
        elif self.choiceId == 6:
            print('正在爬取 ' + url + '\n')
            html = get_html(url)
            data = get_data_chengyu(html)
            self.datas += data

        time.sleep(1)

        if self.choiceId == 0:
            findFG = re.compile(r'(.*?)---', re.S)
            intro = re.findall(findFG, self.datas)[0]
            print('\n' + self.keys + '\n' + intro + '\n点击保存数据以查看\n')
        else:
            print(self.datas + '\n')

    #保存数据
    def save_data(self):
        self.dirs = os.path.join('datas', self.choice, self.keys)
        if os.path.isdir(self.dirs) == False:
            os.makedirs(self.dirs)

        self.fpath = os.path.join(self.dirs, 'contents.txt')
        with open(self.fpath, 'w', encoding='utf-8') as f:
            f.write(self.datas)

        print("数据已保存至 " + self.fpath + '\n\n')

    #生成词云图
    def generate_word_cloud(self):
        title_dict = change_title_to_dict(self.fpath)
        title_dict_sorted = sorted(title_dict.items(), key=lambda x: x[1], reverse=True)  # 将字典按照value值从小到大排序，再逆序

        frequency = "出现频率最高的10个词为：\n"
        for i in range(10):
            frequency += title_dict_sorted[i][0] + "：" + str(title_dict_sorted[i][1]) + "次\n"

        print(frequency + "\n正在生成词云图...\n")
        dict_to_cloud(title_dict, self.dirs, self.keys)
        print("词云图已保存至 " + os.path.join(self.dirs, '词云.png') + '\n\n')

if __name__ == '__main__':
    s = Spider()
    s.search_keys()
    s.save_data()
    s.generate_word_cloud()