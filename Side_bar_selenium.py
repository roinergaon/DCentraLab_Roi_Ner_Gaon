import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CSS selectors for expended and not expended bars
expanded_bar_selector = 'div.duf-aside-bottom-content.sidebar-expanded'
not_expanded_bar_selector = 'div.duf-aside-bottom-content'
@pytest.fixture(scope="session")
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://staging-app.hord.fi/")
    yield driver
    driver.quit()

def test_check_bar_expansion(setup):
    try:
        # Check for expanded_bar_selector element
        WebDriverWait(setup, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, expanded_bar_selector))) #Use timeout instead of just wait sleep
        print("Bar is expanded")
    except:
        # Check for not_expanded_bar_selector element
        try:
            setup.find_element(By.CSS_SELECTOR, not_expanded_bar_selector) # if it get here it already wait for 10 seconds (in the try section)
            print("Bar isn't expanded")
        except:
            # If neither is found, handle accordingly
            print("Elements wasn't found")