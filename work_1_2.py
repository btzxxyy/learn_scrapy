from bs4 import BeautifulSoup

with open('/home/xss/Plan-for-combating/week1/1_2/1_2answer_of_homework/index.html','r') as wb_data:
    soup = BeautifulSoup(wb_data, 'lxml')
    images  = soup.select('div.thumbnail > img')
    prices  = soup.select('div.caption > h4.pull-right')
    titles  = soup.select('div.caption > h4 > a')
    amouts  = soup.select('p.pull-right')
    ratings = soup.select('div.ratings > p:nth-of-type(2)')

info = []



for title, image, price, amout, rating in zip(titles, images, prices, amouts, ratings):

    data = {
        'title' : title.get_text(),
        'image' : image.get('src'),
        'price' : price.get_text(),
        'amout' : amout.get_text(),
        'rating' : len(rating.find_all('span', class_ = 'glyphicon glyphicon-star'))
    }
    info.append(data)

for i in info:
    if float(i['rating']) > 3:
        print(i['title'], i['price'])

# 图片地址、价格、商品标题、评分量、评分星级