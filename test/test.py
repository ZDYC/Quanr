from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests


options = webdriver.ChromeOptions()
# # 添加头部
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument(
	'user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/55.0.2883.103 Safari/537.36"'
	)
options.add_argument("--proxy-server=http://" + "13.231.146.179:443")
# #以相应方式启动
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://user.qunar.com/passport/login.jsp?ret=https%3A%2F%2Fwww.qunar.com%2F")

# proxy = Proxy({
# 'proxyType': ProxyType.MANUAL,
# #代理 ip 和端口
# 'httpProxy': '39.137.69.7:8080'})
# #配置对象 DesiredCapabilities
# dc=DesiredCapabilities.PHANTOMJS.copy()
# #把代理 ip 加入配置对象
# proxy.add_to_capabilities(dc)
# dr=webdriver.PhantomJS(desired_capabilities=dc)
# dr.get('http://httpbin.org/ip')


# r = requests.get('http://httpbin.org/ip', proxies={'http': 'http://85.234.126.107:55555'})
# print(r.text)