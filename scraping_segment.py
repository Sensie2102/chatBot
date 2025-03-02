from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from bs4 import BeautifulSoup


urls = [
    "https://docs.zeotap.com/articles/integrate-customer/sources",
    "https://docs.zeotap.com/articles/integrate-customer/components-of-the-source-listing-page",
    "https://docs.zeotap.com/articles/integrate-customer/knowing-the-fields-on-the-preview-data-tab",
    "https://docs.zeotap.com/articles/integrate-customer/onboard-raw-pii-data-into-zeotap",
    "https://docs.zeotap.com/articles/integrate-customer/source-alerts",
    "https://docs.zeotap.com/articles/integrate-customer/understanding-cookies",
    "https://docs.zeotap.com/articles/integrate-customer/pgp-encryption-in-sources",
    "https://docs.zeotap.com/articles/integrate-customer/destinations",
    "https://docs.zeotap.com/articles/integrate-customer/create-a-destination",
    "https://docs.zeotap.com/articles/integrate-customer/link-an-audience-to-the-destination",
    "https://docs.zeotap.com/articles/integrate-customer/pgp-encryption-in-destinations",
    "https://docs.zeotap.com/articles/integrate-customer/activate-your-real-time-audiences",
    
]


output_dir = "scraped_texts_zeotap"
os.makedirs(output_dir, exist_ok=True)


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")


driver = webdriver.Chrome(options=chrome_options)


exclusion_phrases = [
]

for url in urls:
    print(f"Processing: {url}")
    driver.get(url)
    
    time.sleep(3)
    
    
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    
    for tag in soup.find_all(["header", "footer", "nav", "aside"]):
        tag.decompose()
    
   
    for a in soup.find_all("a"):
        a.decompose()
    
   
    for element in soup(["script", "style"]):
        element.decompose()
    
    text = soup.get_text(separator="\n")
    cleaned_lines = [line.strip() for line in text.splitlines() if line.strip()]
    
    final_lines = [
        line for line in cleaned_lines 
        if not any(phrase in line for phrase in exclusion_phrases)
    ]
    final_clean_text = "\n".join(final_lines)
    
    
    url_part = url.rstrip('/').split('/')[-1]
    filename = f"{url_part if url_part else 'index'}.txt"
    file_path = os.path.join(output_dir, filename)
    
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(final_clean_text)
    
    print(f"Saved cleaned text from {url} to {file_path}")


driver.quit()
