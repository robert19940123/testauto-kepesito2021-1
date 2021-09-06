from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


def test_k4():
    driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html")

    try:

        # TC01
        time.sleep(1.0)
        assert driver.find_elements_by_xpath("//div[@class='flex-child']/p")[2].text \
               == '''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''
        # used only once

        first = driver.find_elements_by_xpath("//form[@onsubmit='return false']/span")[0]
        second = driver.find_elements_by_xpath("//form[@onsubmit='return false']/span")[1]
        third = driver.find_elements_by_xpath("//form[@onsubmit='return false']/span")[2]

        # TC02
        assert first.text in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        assert "+" or "-" in second.text
        assert third.text in "0123456789"

        # TC03

    finally:
        driver.close()
