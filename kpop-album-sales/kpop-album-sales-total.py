# this is my first time learning web scraping with BeautifulSoup
# we will scrape the information for top 100 kpop album sales from https://www.ktown4u.com/totchart100_new?term=total&g_grpNo=1723449
# we will use the BeautifulSoup package 
from platform import release
from bs4 import BeautifulSoup
import requests
import csv

# set https://www.ktown4u.com/totchart100_new?term=total&g_grpNo=1723449 as our source as a text script

source = requests.get('https://www.ktown4u.com/totchart100_new?term=total&g_grpNo=1723449').text

# parse the source with lxml

soup = BeautifulSoup(source, 'lxml')

# we wish to collect the data 
# artist; album_title; release_date; total_sales; 

# each album can be directed to class = list_item
# below will print the first of such class

# album = soup.find('div', class_="list_item")
# album_info = album.find('div', class_="subject")

# let's extract the ranking, artist, title, date and sales for the first album
# rank = album.find('div', class_='info').p.text
# print(rank)

# artist = album_info.find('p', class_='name').text
# print(artist)

# album_title = album_info.find('p', class_='title').text
# print(album_title)

# release_date = album_info.find('p', class_='date').find('span', class_='').text
# print(release_date)

# sales = album_info.find('p', class_='sales').find('span', class_='').text
# print(sales)


### let's create a csv file

csv_file = open('kpop_album_sales_total.csv', 'w', encoding='utf-8')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['ranking', 'artist', 'album_title', 'release_date', 'sales'])


### Next, we will try find_all and gain all the data for the albums

for album in soup.find_all('div', class_='list_item'):
    album_info = album.find('div', class_='subject')
    rank = album.find('div', class_='info').p.text
    print(rank)

    artist = album_info.find('p', class_='name').text
    print(artist)

    album_title = album_info.find('p', class_='title').text
    print(album_title)

    release_date = album_info.find('p', class_='date').find('span', class_='').text
    print(release_date)

    sales = album_info.find('p', class_='sales').find('span', class_='').text
    print(sales)

    print()

    csv_writer.writerow([rank, artist, album_title, release_date, sales])  # this will add the info as row in our csv


csv_file.close()