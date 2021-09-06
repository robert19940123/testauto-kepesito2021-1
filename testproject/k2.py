from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


def test_k2():
    driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html")

    try:

        colors = driver.find_element_by_id("allcolors")
        left_color_name = driver.find_element_by_id("randomColorName")
        left_color_block = driver.find_element_by_id("randomColor")
        right_color_name = driver.find_element_by_id("testColorName")
        right_color_block = driver.find_element_by_id("testColor")
        lower_block = driver.find_element_by_xpath("//br.")
        start = driver.find_element_by_id("start")
        stop = driver.find_element_by_id("stop")
        result = driver.find_element_by_id("result")

        # TC01
        assert "[     ] == [     ]" in lower_block.text
        assert lower_block.is_displayed()
        assert left_color_name.text in colors.text
        assert left_color_block.get_attribute("style")
        assert not right_color_block.get_attribute("style")
        assert not right_color_name.is_displayed()

        # TC02
        start.click()
        time.sleep(1.0)
        assert right_color_block.get_attribute("style")
        assert right_color_name.is_displayed()
        assert right_color_name.text in colors.text
        stop.click()
        time.sleep(1.0)
        assert result.is_displayed()

        # TC03 -- Wanted a "big" while cycle but after every start button press the page getting faster and faster so
        # I decided to make is "slower"
        start.click()
        while True:
            if right_color_name.text == left_color_name.text:
                stop.click()
                time.sleep(0.5)
                assert result.text == "Correct!"
                break

        start.click()
        while True:
            if right_color_name.text != left_color_name.text:
                stop.click()
                time.sleep(0.5)
                assert result.text == "Incorrect!"
                break

    finally:
        driver.close()
