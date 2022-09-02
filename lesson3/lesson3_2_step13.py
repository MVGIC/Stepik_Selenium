import time
import unittest

from selenium import webdriver


class TestClass(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//div/*[@placeholder = 'Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//div/*[@placeholder = 'Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//div/*[@placeholder = 'Input your email']")
        input3.send_keys("test@test.ru")
        button = browser.find_element_by_xpath("//*[@type='submit']")
        button.click()

        time.sleep(5)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(10)
        browser.quit()

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath("//div/*[@placeholder = 'Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_xpath("//div/*[@placeholder = 'Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_xpath("//div/*[@placeholder = 'Input your email']")
        input3.send_keys("test@test.ru")
        button = browser.find_element_by_xpath("//*[@type='submit']")
        button.click()

        time.sleep(5)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(10)
        browser.quit()


if __name__ == "__main__":
    unittest.main()
