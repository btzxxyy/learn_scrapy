from bs4 import BeautifulSoup
import requests

url = 'http://xm.xiaozhu.com/fangzi/1639603035.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
title = soup.select('.pho_info > h4:nth-of-type(1) > em:nth-of-type(1)')
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
    '标题' : title[0].get_text(),
    '地址' : address[0].get_text().replace('\n','').replace(' ',''),
    '租金' : rent_money[0].get_text(),
    '图片' : image[0].get('src'),
    '房东图片' : owner_pic[0].get('src'),
    '房东昵称' : owner_id[0].get_text(),
    '房东性别' : judge_gender(gender)
}

for item in data:
    print(item,data[item])

