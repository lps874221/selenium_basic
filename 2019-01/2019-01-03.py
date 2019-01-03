from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&suggest=1.def.0.V01&wq=sho&pvid=0bb581206a3548078ca8a198de4c5950')
eles = driver.find_elements_by_css_selector('li.gl-item div.p-price')

print(len(eles))

for index in range(len(eles)):
    print(eles[index].text)