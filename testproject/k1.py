from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


def test_k1():
    driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html")

    try:

        a = driver.find_element_by_id("a")
        b = driver.find_element_by_id("b")
        c = driver.find_element_by_id("result")

        # TC01
        assert a.text == ""
        assert b.text == ""
        assert not c.is_displayed()

        def solution(one, two, three):
            a.clear()
            b.clear()
            a.send_keys(one)
            b.send_keys(two)
            driver.find_element_by_id("submit").click()  # used only once
            time.sleep(0.5)
            assert c.text == three

        # TC02
        solution("2", "3", "10")

        # TC03
        solution("", "", "NaN")

    finally:
        driver.close()
