import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Path to ChromeDriver
chrome_driver_path = "chromedriver.exe"
service = Service(chrome_driver_path)

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
driver = webdriver.Chrome(service=service, options=options)

# URLs for scraping
URLS = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

scraped_data = {}

for cdp, url in URLS.items():
    driver.get(url)
    
    # Adjust this selector according to the site's structure
    elements = driver.find_elements(By.TAG_NAME, "h2")

    for el in elements:
        question = el.text.strip()
        if question:
            scraped_data[question] = f"Refer to {cdp} documentation at {url}"

# Save scraped data
with open("scraped_data.json", "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, indent=4)

driver.quit()
print("Scraping completed and saved to scraped_data.json")
