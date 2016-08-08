from bs4 import BeautifulSoup
import time
import requests
import os


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部\\
    path = path.strip('\\')
    # 判断路径是否存在
    # 存在    True
    # 不存在  False
    is_exists = os.path.exists(path)

    if not is_exists:
        # 如果不存在则创建目录
        print(path + '创建成功')
        # 创建目录操作函数
        os.mkdir(path)
    else:
        # 如果目录存在则不创建并提示已存在
        print(path + '已存在')
        return False

mkpath = '.\\Taylor\\'
mkdir(mkpath)


def get_pic_url():
    pic_urls = []
    for i in range(1, 11):
        main_url = 'http://weheartit.com/inspirations/taylorswift?page={}'.format(i)
        time.sleep(0.1)
        wb_data = requests.get(main_url)
        if wb_data.status_code != 200:
            continue
        soup = BeautifulSoup(wb_data.text, 'lxml')
        pic_url_raw = soup.select('img.entry-thumbnail')
        for a_url in pic_url_raw:
            pic_urls.append(a_url.get('src'))
    return pic_urls


def down(a_url):
    pic_res = requests.get(a_url)
    if pic_res.status_code != 200:
        return
    filename = a_url.split('/')[-2] + '.' + a_url.split('.')[-1]
    target = './Taylor/' + filename
    with open(target, 'wb') as pic_file:
        pic_file.write(pic_res.content)
    print('%s => %s' % (url, target))


for url in get_pic_url():
    down(url)
    time.sleep(0.1)




