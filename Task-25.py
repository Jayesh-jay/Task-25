from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys


class Imdb:
    def search_all(self, search_results, from_date, to_date, bday):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://www.imdb.com/search/name/")
        wait = WebDriverWait(driver, 15)
        actions = ActionChains(driver)

        # Page down to avoid auto scrolling after each Data entry
        for _ in range(15):
            actions.send_keys(Keys.DOWN).perform()

        # Input Boxes
        name_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Name']")))
        name_box.click()
        enter_name_box = wait.until(EC.presence_of_element_located((By.NAME, "name-text-input")))
        enter_name_box.send_keys(search_results)

        for _ in range(5):
            actions.send_keys(Keys.DOWN).perform()

        # Select Boxes - Birth_date
        birth_date = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Birth date']")))
        birth_date.click()
        enter_from_date = wait.until(EC.presence_of_element_located((By.NAME, "birth-date-start-input")))
        enter_from_date.send_keys(from_date)
        enter_to_date = wait.until(EC.presence_of_element_located((By.NAME, "birth-date-end-input")))
        enter_to_date.send_keys(to_date)

        for _ in range(5):
            actions.send_keys(Keys.DOWN).perform()

        # Birthday
        birth_day = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Birthday']")))
        birth_day.click()
        day_text_box = wait.until(EC.presence_of_element_located((By.NAME, 'birthday-input')))
        day_text_box.send_keys(bday)

        # Click Search button
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button/span[text()="See results"]')))
        search_button.click()

        exp_url = "https://www.imdb.com/search/name/?name=Tom%20Cruise&birth_date=1962-07-03,2024-07-03&birth_monthday=07-03"

        # Wait for search results page to load
        if driver.current_url == exp_url:
            print(f"SUCCESS: Performed {search_results} Name Search")

        # Close browser window
        driver.quit()


imdb_search = Imdb()
imdb_search.search_all("Tom Cruise", "03-07-1962", "03-07-2024", "07-03")
