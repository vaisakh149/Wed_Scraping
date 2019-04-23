#!/usr/bin/env python
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import itertools
import re
url="https://techolution.app.param.ai/jobs/"
driver = webdriver.Firefox()
driver.get(url) 
html= driver.execute_script("return document.documentElement.outerHTML")
# print(html)
sel_soup =BeautifulSoup(html,'html.parser')
containers =sel_soup.findAll("div", {"class":"ui segments"})
# print((containers))
# print(BeautifulSoup.prettify(containers[0]))
container=containers[0]
# qualification=containers.div.h2
# print(qualification)
# jobname=container.find('h3')
#print(jobname.text)

# location=container.findAll('h2')
# data=location.text
# print(data)
i=0
while i<(len(containers)-1):
	for location in containers[i].find_all('h2'):
		print(location.text)
	i+=1