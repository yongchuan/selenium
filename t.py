#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
#import chardet
import os
import sys
#from bs4 import BeautifulSoup

import traceback 
import urlparse

from model.product import Product

from pyvirtualdisplay import Display
from selenium.webdriver.common.proxy import *

from multiprocessing import Process
from multiprocessing import Pool

#display = Display(visible=0, size=(800, 600))
#display.start()

reload(sys)
sys.setdefaultencoding('utf-8')

def addslashes(s):
	d = {'"':'\\"', "'":"\\'", "\0":"\\\0", "\\":"\\\\"}
	return ''.join(d.get(c, c) for c in s)

def scroll(driver, type="down"):
	height = 100;
	if type == "down":
		js = 'document.documentElement.scrollTop=document.documentElement.scrollTop+' + str(height) +';';
	else:
		js = 'document.documentElement.scrollTop=document.documentElement.scrollTop-' + str(height) +';';
	driver.execute_script(js)

def getHtml(driver):
	js = "var input = document.createElement('div'); "
	js += 'input.setAttribute("id", "source"); '
	js += 'var s = document.getElementsByTagName("html")[0].innerHTML; '
	js += 'input.setAttribute("s", s); '
	js += 'document.getElementById("header").appendChild(input);'
	driver.execute_script(js)
	return driver.find_element_by_id("source").get_attribute("s")
	
def getContent(driver, url):
	driver.get(url)
	j = 0
	k = 0
	while True:
		j = j+1
		for i in range(0, 150):
			scroll(driver=driver)
		start = j * 10;
		for i in range(0, start):
			scroll(driver=driver, type="up")	
		try:
			score = driver.find_element_by_class_name("ui-page")
			if score:
				break;
		except:	
			k = k + 1
			if k > 20:
				break;
			print "expect"		
	content = getHtml(driver=driver)
	content = "<!doctype html><html>" + content + "</html>"
	return content
	

driver = webdriver.Firefox()
driver.maximize_window()
url = 'https://list.tmall.com/search_product.htm?cat=54436007&sort=s&style=g&search_condition=7&from=sn_1_cat&active=1&industryCatId=50105688&spm=a2224.1382173.1998187256.1.4kNkAK&tmhkmain=0#J_crumbs'
print url
getContent(driver, url)
page = driver.find_element_by_xpath("//input[@name='totalPage']");
pageCount = page.get_attribute('value')
for i in range(int(pageCount)):
	try:
		items = driver.find_element_by_id("J_ItemList").find_elements_by_class_name("product");
		values = {}
		for tmp in items:
			url = tmp.find_element_by_tag_name('a').get_attribute('href')
			shopUrl = tmp.find_element_by_class_name('productShop').find_element_by_tag_name('a').get_attribute('href')
			result = urlparse.urlparse(url)
			params = urlparse.parse_qs(result.query,True)
			iid = params['id']
			result = urlparse.urlparse(shopUrl)
			params = urlparse.parse_qs(result.query,True)
			if params.has_key('user_number_id'):
				shopUserId = params['user_number_id']
			else:
				shopUserId = 0
			print iid 
			print shopUserId
			print url
			print shopUrl
	except Exception, e:		
		print e
		print 'aaa'
