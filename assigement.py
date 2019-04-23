#!/usr/bin/env python
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
i=0
url="https://techolution.app.param.ai/jobs/"
driver = webdriver.Firefox()
driver.get(url) 
html= driver.execute_script("return document.documentElement.outerHTML")
# print(html)
sel_soup =BeautifulSoup(html,'html.parser')
containers =sel_soup.findAll("div", {"class":"ui segments"})
# print(len(containers))
Data=pd.DataFrame()
while i<(len(containers)):
	for department in containers[i].find_all('h2'):
		# print(department)
		for position in containers[i].find_all('h3'):
			{}
		for days in containers[i].find_all('span',{'class':'date_posted'}):
			{}
		for pargraph in containers[i].find_all('p'):
			y=pargraph.text.split()
			data=pd.DataFrame({'jd':[y],'Department':[department.text],'position':[position.text], 'days':[days.text]})
			if i==0:
				Data=data
			else:
				Data=Data.append(data)
	i=i+1
print(Data)
Data.to_csv('sample.csv', header=True, index=False) 
