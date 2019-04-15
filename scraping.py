from bs4 import BeautifulSoup
from urllib.request import urlopen
#my_url='https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
my_url='https://techolution.app.param.ai/jobs/'

uClient = urlopen(my_url)
page_html =uClient.read()
uClient.close()
page_soup =BeautifulSoup(page_html,"html.parser")
#BeautifulSoup.select("div.classname1.classname2")
containers =page_soup.findAll("div")
	#, {"class":"bhgxx2 col-12-12"})
print((containers))


