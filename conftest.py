import pytest
from selenium import webdriver
from Data.url import main_site


@pytest.fixture(params=[ 'firefox', 'chrome'], scope="function")
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    driver.get(main_site)
    yield driver
    driver.quit()
