from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)


def test_k5():
    driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html")

    try:

        tickets = driver.find_elements_by_xpath("//tbody/tr/td/input")
        boxes = driver.find_elements_by_xpath("//ol/li/input")

        # TC01
        assert len(tickets) == 25
        assert len(boxes) == 75

        # TC02
        spin = driver.find_element_by_id("spin")

        while True:
            spin.click()
            if driver.find_element_by_id("messages").text == "BINGO":
                break

        # number = 0
        # for box in boxes:
        #     if box.get_attribute("value") == tickets[number]:
        #         assert box.get_attribute("value") and tickets[number]

        # TC03
        old_numbers = []
        for ticket in tickets:
            old_numbers.append(ticket.get_attribute("value"))

        driver.find_element_by_id("init").click()
        time.sleep(0.5)

        new_numbers = []
        tickets = driver.find_elements_by_xpath("//tbody/tr/td/input")
        for _ in tickets:
            new_numbers.append(_.get_attribute("value"))

        assert old_numbers != new_numbers

    finally:
        driver.close()
