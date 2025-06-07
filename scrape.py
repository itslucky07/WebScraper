from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching Chrome browser")

    options = Options()
    options.add_argument("--headless")  # run without GUI
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    with webdriver.Chrome(options=options) as driver:
        print("Connected! Navigating...")
        driver.get(website)

        print("Taking page screenshot to file page.png")
        driver.get_screenshot_as_file('./page.png')

        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html  # ✅ Return HTML content

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    return str(body_content) if body_content else ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]
