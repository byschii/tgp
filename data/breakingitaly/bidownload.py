from pytube import YouTube, Channel
from bs4 import BeautifulSoup
import requests
from playwright.sync_api import Playwright, sync_playwright
import time

# scrape youtube channel for video links with playwright
def run(playwright: Playwright, url:str) -> None:
    content = ""
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    goto_url = url or "https://consent.youtube.com/m?continue=https%3A%2F%2Fwww.youtube.com%2F%40breakingitaly%2Fvideos%3Fcbrd%3D1&gl=IT&m=0&pc=yt&cm=2&hl=en&src=1"
    page.goto(goto_url)
    page.get_by_role("button", name="Accept all").click()

    # wait for page to load
    page.wait_for_load_state("networkidle")

    # scroll down to load more videos
    for i in range(20):
        print("scrolling down", i)
        time.sleep(2)
        #page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
        page.mouse.wheel(0, 250)
        

    # extract page content
    content = page.content()

    context.close()
    browser.close()

    return content

DESTINATION = "bi.html"
with sync_playwright() as playwright:
    content = run(playwright, "https://www.youtube.com/@breakingitaly/videos")
    with open(DESTINATION, "w+") as f:
        f.write(content)