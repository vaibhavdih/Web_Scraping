from bs4 import BeautifulSoup
from selenium import webdriver
import time

def get_name(section):
	name_div =  section.find('div',{'class':'section-result-title-container'})
	if name_div is not None:
		return name_div.h3.text.strip()
	else:
		return None

def get_rating(section):
	rating_div =  section.find('span',{'class':'section-result-rating'})
	if rating_div is not None:
		return rating_div.text.strip()
	else:
		return None

def get_address(section):
	address_div =  section.find('span',{'class':'section-result-location'})
	if address_div is not None:
		return address_div.text.strip()
	else:
		return None

def get_open_hours(section):
	hours_div =  section.find('span',{'class':'section-result-opening-hours'})
	if hours_div is not None:
		return hours_div.text.strip()
	else:
		return None

def get_phone(section):
	phone_div =  section.find('span',{'class':'section-result-phone-number'})
	if phone_div is not None:
		return phone_div.span.text.strip()
	else:
		return None

def get_img_url(section):
	img_div =  section.find('div',{'class':'section-result-image'})
	if img_div is not None:
		return img_div.get('style')[21:-1]
	else:
		return None

def get_places(url):
	driver = webdriver.Chrome()
	driver.get(url);
	time.sleep(10)
	button = driver.find_elements_by_xpath('//*[@id=\"n7lv7yjyC35__section-pagination-button-next\"]/span')[0]
	while(True):
		places = driver.find_element_by_class_name("section-layout-flex-vertical")
		details = places.find_element_by_class_name("section-layout-flex-vertical")
		data = details.get_attribute("outerHTML")
		soup = BeautifulSoup(data, 'html.parser')
		sections = soup.findAll('div', {'class':'section-result-content'})
		for section in sections:
			name = get_name(section)
			rating = get_rating(section)
			address = get_address(section)
			open_hours = get_open_hours(section)
			phone_no = get_phone(section)
			img_url = get_img_url(section)

			if name is not None:
				print(name)
			if rating is not None:
				print(rating)
			if address is not None:
				print(address)
			if open_hours is not None:
				print(open_hours)
			if phone_no is not None:
				print(phone_no)
			if img_url is not None:
				print(img_url)
			print("----------------------------------------")
		try:
			button.click()
			time.sleep(2)
		except:
			print('---Finished---')
			driver.quit()
			break

url = 'https://www.google.com/maps/search/medical+shops+in+udaipur/'
get_places(url)
