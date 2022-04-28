from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

base_url = "https://www.zacks.com/stock/research/GLOP/earnings-calendar?tab=dividends"

def main():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    body = driver.get(base_url)
    content = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    table = content.find("table", {"id": "earnings_announcements_dividends_table"})
    # print(content.prettify())
    print(table)


if __name__ == '__main__':
    main()
