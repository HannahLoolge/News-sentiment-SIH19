#this is a scrapper of Times of India news website
import requests
from bs4 import BeautifulSoup as bsp #pip install beautifulsoup4
page = requests.get('https://www.thehindu.com/search/?q=railways&order=DESC&sort=publishdate&pd=yesterday&ct=text&page=1') #the toi railways topic link
data = page.text
soup= bsp(data,'html.parser')
#print(soup)
results = soup.findAll("div", {"class" : "75_1x_StoryCard mobile-padding"})
#print (results)
for tag in results:
#  	#soup=bsp(tag)
 	headline = tag.find("a", {"class" : "story-card75x1-text"})
 	print(headline.string)
# 	date_time= tag.find("span",{"class" : "meta"})
# 	print(date_time.string)
# 	#date_time_formatted= date_time.string
# 	print('\n')
