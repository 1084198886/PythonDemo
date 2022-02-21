"""
邮箱自动登录
"""

from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions

#
# opts1 = ChromiumOptions()
# opts1.binary_location = 'D:\AppInstall\ChromeCore\ChromeCore.exe'

a = webdriver.Chrome()
a.get('https://mail.163.com/')

iframe = a.find_element('iframe')
a.switch_to.frame(iframe)

iframe.find_element_by_name('email').send_keys()
