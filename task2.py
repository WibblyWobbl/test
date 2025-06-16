from playwright.sync_api import sync_playwright

TITLE = "Fast and reliable end-to-end testing for modern web apps | Playwright"
LINK = "https://playwright.dev/"

def check_title(browser_type):
    try:
        with browser_type.launch() as browser:
            page = browser.new_page()
            page.goto(LINK)
            title_element = page.locator(".hero__title")
            title_element.wait_for(state="visible") 
            title = page.title()
            print(f"title in {browser_type.name} - {title},\nexpected_title - {TITLE}")
            assert title == EXPECTED_TITLE
            print(f"correct title in {browser_type.name}\n")

    except Exception as e:
        print(f"error using {browser_type.name}\n")


with sync_playwright() as sp:
    check_title(sp.chromium)
    check_title(sp.firefox)
