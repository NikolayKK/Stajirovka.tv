from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def test_example_domain():
    options = Options()
    options.add_argument('--headless')  # для запуска без окна браузера
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://example.com")

        # Проверка заголовка
        assert "Example" in driver.title

        # Поиск и клик по ссылке
        link = driver.find_element(By.CSS_SELECTOR, "a[href='https://www.iana.org/help/example-domains']")
        link.click()

        time.sleep(1)  # Подождём немного

        # Проверка редиректа
        assert driver.current_url == "https://www.iana.org/help/example-domains"
        print("Тест пройден успешно!")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_example_domain()
