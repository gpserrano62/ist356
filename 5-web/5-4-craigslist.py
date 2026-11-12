from playwright.sync_api import Playwright, sync_playwright
import json 
import os

PAGE_CACHE = "/workspace/5-web/cache/"
BASE_URL = "https://www.craigslist.org/search/area/syracuse?cat=sss&query={search}#search=2~list~0"
TITLE_SELECTOR = "#search-results-1 > div:nth-child({i}) > div > div > a"
PRICE_SELECTOR = "#search-results-1 > div:nth-child({i}) > div > div > div > span.priceinfo"
LOCATION_SELECTOR = "//html//body//div[1]//main//div[1]//div[4]//div[2]//div[3]//div[{i}]//div//div//div//span[2]"

def scrape_craigslist(playwright: Playwright, 
                      search:str, ignore_cache: bool = False, 
                      max_results: int = 10) -> list[dict]:
    cache_file = os.path.join(PAGE_CACHE, f"craigslist-{search}.html")    
    browser = playwright.chromium.launch(headless=False)
    # simulate a real browser user agent to avoid being blocked by Craigslist
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    context = browser.new_context(user_agent=user_agent)
    page = context.new_page()
    url = BASE_URL.format(search=search)
    if not ignore_cache and os.path.exists(cache_file):
        print(f"Cache hit on {search}, using cached file: {cache_file}")
        page.goto(f"file://{cache_file}")
    else:
        print(f"Cache miss on {search}, scraping the Craigslist page")
        page.goto(url)
        page.wait_for_selector("#search-results-1")
        # save to cache
        print(f"Saving page content to cache: {cache_file}")
        with open(cache_file, 'w') as f:
            f.write(page.content())

    # grab elements from the page
    page.wait_for_selector("#search-results-1")
    items = []
    for i in range(2, max_results + 2):
        link = page.query_selector(TITLE_SELECTOR.format(i=i))
        title = link.inner_text()
        url = link.get_attribute("href") # no good to reuse
        price = page.query_selector(PRICE_SELECTOR.format(i=i)).inner_text()
        location = page.query_selector(LOCATION_SELECTOR.format(i=i)).inner_text()
        item = {
            "title": title,
            "price": price,
            "location": location,
            "link": url
        }
        items.append(item)

    return items 

if __name__ == "__main__":
    with sync_playwright() as playwright:
        scrape_craigslist(playwright, "tires", ignore_cache=False)
