import time

from selenium import webdriver

# 设置浏览器默认语言为英语
options = webdriver.ChromeOptions()
options.add_argument('lang=en.UTF-8')
browser = webdriver.Chrome(chrome_options=options)

browser.get("https://www.google.com.hk/search?")

browser.find_element_by_name("q").send_keys("中国首都的经纬度\n")

time.sleep(5)
browser.quit()
