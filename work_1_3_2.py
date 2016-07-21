from bs4 import BeautifulSoup
import requests
import time
import re

n = 1
urls = []
a_url = 'http://sh.xiaozhu.com/search-duanzufang-p' + str(n) + '-0/'
# 从主页上爬取指向房源的链接
while n < 15:
    homepage = requests.get(a_url)
    homepage_soup = BeautifulSoup(homepage.text, 'lxml')
    links = homepage_soup.find_all(href=re.compile("fangzi"))
    for link in links:
        a_link = link.get('href')
        urls.append(a_link)
    n += 1

print(len(urls))


def get_url(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    return soup


def get_data(soup):
    title = soup.select('.pho_info > h4:nth-of-type(1) > em')
    address = soup.select('.pr5')
    rent_money = soup.select('.day_l')
    image = soup.select('#curBigImage')
    owner_pic = soup.select('.member_pic > a > img')
    owner_id = soup.select('a.lorder_name')
    owner_gender = soup.select('.member_pic > div')

    gender = owner_gender[0].get('class')[0]

    def judge_gender(a_gender):
        if a_gender == 'member_ico1':
            return '女'
        else:
            return '男'

    data = {
        '标题': title[0].get_text(),
        '地址': address[0].get_text().replace('\n', '').replace(' ', ''),
        '租金': rent_money[0].get_text(),
        '图片': image[0].get('src'),
        '房东图片': owner_pic[0].get('src'),
        '房东昵称': owner_id[0].get_text(),
        '房东性别': judge_gender(gender)
    }
    return data

if __name__ == '__main__':
    j = 0
    for url in urls:
        soup = get_url(url)
        print(get_data(soup))
        j += 1
    print("总共获取了%d个房源的信息"%j)


