import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def login_session():
    

        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_timeout(3000)
        page.wait_for_url("**/inventory.html")
        page.click("#react-burger-menu-btn")
        page.click("#logout_sidebar_link")

        yield page
