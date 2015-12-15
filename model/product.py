#coding:utf-8
class Product:
	def getHtml(self, driver):
		js = "var input = document.createElement('div'); "
		js += 'input.setAttribute("id", "m_desc"); '
		js += 'var s = document.getElementById("description").innerHTML; '
		js += 'input.setAttribute("s", s); '
		js += 'document.getElementById("header").appendChild(input);'
		driver.execute_script(js)
		return driver.find_element_by_id("m_desc").get_attribute("s")
	
	def getTitle(self, driver):
		try:
			title = driver.find_element_by_class_name("tb-detail-hd").find_element_by_tag_name("h1").text;
			return title
		except:		
			return ''
		
	def getSubTitle(self,driver):
		try:
			value = driver.find_element_by_class_name("newp").text;
			return value
		except:		
			return ''
			
	def getPrice(self,driver):
		try:
			value = driver.find_element_by_class_name("tm-tagPrice-panel").find_element_by_class_name("tm-price").text;
			return value
		except:	
			value = ""
		
		try:
			value = driver.find_element_by_id("J_StrPriceModBox").find_element_by_class_name("tm-price").text;
			return value
		except:
			return ""
			
	def getPromotePrice(self,driver):
		try:
			value = driver.find_element_by_class_name("tm-promo-price").find_element_by_class_name("tm-price").text;
			return value
		except:		
			return ''
			
	def getMonthSaleCount(self,driver):
		try:
			value = driver.find_element_by_xpath("//li[@data-label='月销量']").find_element_by_class_name("tm-count").text;
			return value
		except:		
			return ''
			
	def getCommentCount(self,driver):
		try:
			value = driver.find_element_by_id("J_ItemRates").find_element_by_class_name("tm-count").text;
			return value
		except:		
			return ''

	def getStock(self,driver):
		try:
			value = driver.find_element_by_id("J_EmStock").text;
			value = value.replace("库存", "").replace("件","")
			return value
		except:		
			return ''
		
	def getCollectCount(self,driver):
		try:
			value = driver.find_element_by_id("J_CollectCount").text;
			value = value.replace("（", "").replace("人气）","")
			return value
		except:		
			return ''
			
	def getBrandName(self,driver):
		try:
			value = driver.find_element_by_class_name("J_EbrandLogo").text;			
			return value
		except:		
			return ''
			
	def getBrandUrl(self,driver):
		try:
			value = driver.find_element_by_class_name("J_EbrandLogo").get_attribute("href");			
			return value
		except:		
			return ''
			
	def getScore(self,driver):
		try:
			value = driver.find_element_by_class_name("rate-score").find_element_by_tag_name("strong").text;			
			return value
		except:		
			return ''
	
	def getScoreExtra(self,driver):
		try:
			items = driver.find_element_by_class_name("rate-tag-inner").find_elements_by_tag_name("span");
			values = []
			for tmp in items:
				txt = tmp.text
				txtArr = txt.split('(')
				tmpTxt = txtArr[0] + ":" + txtArr[1].replace(")", "")
				values.append(tmpTxt)
			return '|'.join(values)
		except:		
			return ''
		
	def getDescription(self,driver):
		try:
			value = self.getHtml(driver=driver)
			return value
		except:		
			return ''
			
	def getAttr(self,driver):
		try:
			items = driver.find_element_by_id("J_AttrUL").find_elements_by_tag_name("li");
			values = {}
			for tmp in items:
				txt = tmp.text
				txtArr = txt.split('：')	
				if len(txtArr) != 2:
					txtArr = txt.split(':')
				values[txtArr[0]] = txtArr[1]
			return values
		except:		
			return {}
	
	def getSku(self,driver):
		try:
			items = driver.find_element_by_class_name("tb-sku").find_elements_by_tag_name("dl")
			values = {}
			for tmp in items:
				skuName = tmp.find_element_by_tag_name('dt').text
				skuValueItems = tmp.find_element_by_tag_name('ul').find_elements_by_tag_name("li")
				skuValues = []
				for tmp2 in skuValueItems:
					skuValue = tmp2.text
					skuValues.append(skuValue)
				values[skuName] = skuValues
			return values
		except:		
			return {}
	
	def getImg(self, driver):
		try:
			items = driver.find_element_by_id("J_UlThumb").find_elements_by_tag_name("li")
			values = []
			for tmp in items:
				url = tmp.find_element_by_tag_name('img').get_attribute('src')
				values.append(url)
			return values
		except:		
			return {}
	
	def getShopRefound(self, driver):
		try:
			value = driver.find_element_by_class_name("serviceQuality").find_elements_by_tag_name('li')[0].find_element_by_class_name('desc').text
			return value
		except:					
			return ''
			
	def getShopDispute(self, driver):
		try:
			value = driver.find_element_by_class_name("serviceQuality").find_elements_by_tag_name('li')[1].find_element_by_class_name('desc').text
			return value
		except:				
			return ''
	
	def getShopComplain(self, driver):
		try:
			value = driver.find_element_by_class_name("serviceQuality").find_elements_by_tag_name('li')[2].find_element_by_class_name('desc').text
			return value
		except:				
			return ''
			
	def getShopPunish(self, driver):
		try:
			value = driver.find_element_by_class_name("serviceQuality").find_elements_by_tag_name('li')[3].find_element_by_class_name('desc').text
			return value
		except:				
			return ''
			
	def getScoreDesc(self, driver):
		try:
			value = driver.find_element_by_id("J_sellerRateInfo").find_elements_by_tag_name('li')[0].find_element_by_class_name('count').text
			level = driver.find_element_by_id("J_sellerRateInfo").find_elements_by_tag_name('li')[0].find_element_by_tag_name('strong').text
		
			return value + ":" + level
		except:				
			return ''
	
	def getScoreService(self, driver):
		try:
			value = driver.find_element_by_id("J_sellerRateInfo").find_elements_by_tag_name('li')[1].find_element_by_class_name('count').text
			level = driver.find_element_by_id("J_sellerRateInfo").find_elements_by_tag_name('li')[1].find_element_by_tag_name('strong').text
			return value + ":" + level
		except:				
			return ''
			
	def getScoreShip(self, driver):
		try:
			value = driver.find_element_by_id("J_sellerRateInfo").find_elements_by_tag_name('li')[2].find_element_by_class_name('count').text
			level = driver.find_element_by_id("J_sellerRateInfo").find_elements_by_tag_name('li')[2].find_element_by_tag_name('strong').text
			
			return value + ":" + level
		except:				
			return ''
			
	def getTmShopIdUserId(self, driver):
		try:
			value = driver.find_element_by_xpath("//meta[@name='microscope-data']").get_attribute('content')
			arr1 = value.split(';')
			shopId = 0
			userId = 0
			for i in arr1:
				tmp = i.split('=')
				if tmp[0].strip() == 'shopId':
					shopId = tmp[1]
				if tmp[0].strip() == 'userid':
					userId = tmp[1]
			
			return shopId + ':' + userId
		except:				
			return ''
	
