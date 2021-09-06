from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


def test_k3():
    driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html")

    try:

        input_field = driver.find_element_by_id("title")
        error_field = driver.find_element_by_xpath("//span[@aria-live='polite']")

        # TC01
        input_field.send_keys("abcd1234")
        assert not error_field.is_displayed()

        def solution(a, b):
            time.sleep(0.5)
            input_field.clear()
            input_field.send_keys(a)
            assert error_field.text == b

        # TC02
        solution("teszt233@", "Only a-z and 0-9 characters allewed")

        # TC03
        solution("abcd", "Title should be at least 8 characters; you entered 4.")

    finally:
        driver.close()
