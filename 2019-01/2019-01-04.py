from selenium import webdriver
from datetime import datetime
import xlwt
driver = webdriver.Chrome()

driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=1.def.0.V01&wq=sho&pvid=0bb581206a3548078ca8a198de4c5950')
price_eles = driver.find_elements_by_css_selector('li.gl-item div.p-price')
desc_eles = driver.find_elements_by_css_selector('div.p-name.p-name-type-2')

count = len(price_eles)
wd = xlwt.Workbook()
ws = wd.add_sheet('jd手机')

ws.write(0,0,'手机')
ws.write(0,1,'价格')

for index in range(count):
    ws.write(index+1,0, desc_eles[index].text)
    ws.write(index+1,1, price_eles[index].text)

wd.save('phone.xls')
    

