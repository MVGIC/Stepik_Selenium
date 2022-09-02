import math
import time

import pytest


@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_find_ufo(browser, links):
    link = f"https://stepik.org/lesson/{links}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    browser.find_element_by_class_name("ember-text-area").send_keys(answer)
    browser.find_element_by_class_name("submit-submission").click()

    feedback = browser.find_element_by_class_name("smart-hints").text
    assert feedback == "Correct!", "опциональный фидбек не совпадает"
