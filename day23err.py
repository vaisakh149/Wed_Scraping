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
	print(i)
	for department in containers[i].find_all('h2'):
		# print(department)
		print("in for1 loop")
		for position in containers[i].find_all('h3'):
			# print("in for2 loop")
			for days in containers[i].find_all('span',{'class':'date_posted'}):
				print(days)
				data=pd.DataFrame([[department.text,position.text,days.text]])
				if i==0:
					# print("in if loop")
					Data=data
				else:
					Data=Data.append(data,ignore_index=True)
	i=i+1
print(Data)
