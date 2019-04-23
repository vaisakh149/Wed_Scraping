#!/usr/bin/env python
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import itertools
import re
url="https://techolution.app.param.ai/jobs/"
'''
web_r=requests.get(url)
web_soup =BeautifulSoup(web_r.text,'html.parser')
print(web_soup.findAll("class"))
'''
driver = webdriver.Firefox()
driver.get(url) 
html= driver.execute_script("return document.documentElement.outerHTML")
print(html)
# sel_soup =BeautifulSoup(html,'html.parser')
# containers =sel_soup.findAll("div", {"class":"ui segments"})
# print((containers))
#print(BeautifulSoup.prettify(containers[0]))
# container=containers[0]
# qualification=containers.div.h2
# print(qualification)
# jobname=container.find('h3')
#print(jobname.text)

# location=container.find("div", {"class":"twelve wide computer twelve wide tablet sixteen wide mobile column"})
# data=location
# print(data)
