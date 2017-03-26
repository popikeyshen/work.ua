from bs4 import BeautifulSoup
from urllib2 import urlopen
 
filename = 'work_ua.csv'
f = open(filename,'w')
headers = 'title,price\n'
f.write(headers)

block=[]

i=0
while i<2000:

	i=i+1
	html = urlopen('https://www.work.ua/jobs-kyiv/?page='+ str(i) ).read()
	soup = BeautifulSoup(html,'lxml')

	for conteiners in soup.find_all('div',{'class', 'card card-hover card-visited job-link card-logotype'}):

		title=conteiners.find('a').text.encode('utf-8')

		zp=conteiners.find_all('span')[2].text.encode('utf-8')

		#block.append([[title],[zp]])

		f.write(title.replace(',',' ').replace('\n',' ') + ',' + zp.replace(',',' ').replace('\n',' ') + '\n')

		#print title
		#print zp

f.close






	




