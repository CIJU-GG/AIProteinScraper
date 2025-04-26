from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from pathlib import Path
# Add imports for alternative methods
import requests
from urllib3 import ProxyManager, PoolManager
import urllib3
import random
import time

dotenv_path = Path('sample.env')
load_dotenv(dotenv_path=dotenv_path)

SBR_WEBDRIVER = os.getenv("SBR_WEBDRIVER")
# Add environment variables for alternative proxy methods
AZURE_PROXY_URL = os.getenv("AZURE_PROXY_URL", None)
PROXY_USERNAME = os.getenv("PROXY_USERNAME", None)
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD", None)

def scrape_website(website):
    print(f"SBR_WEBDRIVER: {SBR_WEBDRIVER}")
    print("Connecting to Scraping Browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html

# New alternative methods using different proxy approaches

def scrape_with_urllib3_proxy(website):
    """
    Use urllib3's ProxyManager to make requests through a proxy
    """
    print(f"Using proxy: {AZURE_PROXY_URL}")
    if not AZURE_PROXY_URL:
        print("No proxy URL configured. Using direct connection.")
        http = PoolManager()
    else:
        # Configure proxy with authentication if provided
        proxy_headers = {}
        if PROXY_USERNAME and PROXY_PASSWORD:
            auth = urllib3.util.request.make_headers(
                proxy_basic_auth=f"{PROXY_USERNAME}:{PROXY_PASSWORD}"
            )
            proxy_headers.update(auth)
        
        http = ProxyManager(AZURE_PROXY_URL, headers=proxy_headers)
    
    try:
        # Add random user agent to avoid detection
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ]
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml',
        }
        
        response = http.request('GET', website, headers=headers, timeout=30.0)
        return response.data.decode('utf-8')
    except Exception as e:
        print(f"Error fetching {website}: {str(e)}")
        return None

def scrape_with_requests(website):
    """
    Use requests library with proxy support
    """
    proxies = {}
    if AZURE_PROXY_URL:
        if PROXY_USERNAME and PROXY_PASSWORD:
            proxy_with_auth = AZURE_PROXY_URL.replace('http://', f'http://{PROXY_USERNAME}:{PROXY_PASSWORD}@')
            proxies = {
                "http": proxy_with_auth,
                "https": proxy_with_auth
            }
        else:
            proxies = {
                "http": AZURE_PROXY_URL,
                "https": AZURE_PROXY_URL
            }
    
    try:
        # Add random delay and user agent to avoid detection
        time.sleep(random.uniform(1, 3))
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
        ]
        headers = {
            'User-Agent': random.choice(user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml',
        }
        
        response = requests.get(
            website, 
            proxies=proxies, 
            headers=headers,
            timeout=30
        )
        return response.text
    except Exception as e:
        print(f"Error fetching {website}: {str(e)}")
        return None

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
