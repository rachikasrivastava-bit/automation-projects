from playwright.sync_api import Page, expect, sync_playwright 

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))
from Login_page import LoginPage
from Cart_page import SortAddCart
from Checkout import Checkout_Page



def test_e2e(page: Page):
    # Initialize Page Objects
    login_page = LoginPage(page)
    cart_page = SortAddCart(page)
    checkout_page = Checkout_Page(page)
    

    # Execution Flow
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    page.wait_for_timeout(2000)

    cart_page.sort_and_add_to_cart()
    page.wait_for_timeout(2000)
    
    cart_page.go_to_cart()
    cart_page.proceed_to_checkout()

    checkout_page.fill_information("John", "Doe", "12345")
    checkout_page.complete_checkout()

    # Final Assertion
    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        test_e2e(page)
        #browser.close()