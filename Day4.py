#First Pytest

# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#    browser = p.chromium.launch(headless=False)
#    page = browser.new_page()
#    page.goto('https://google.com')
#    print(page.title())
#    browser.close()

#===================================================================================

# from playwright.sync_api import sync_playwright

# def test_google_title():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()

#         page.goto("https://www.google.com")

#         assert page.title() == "Google"

#         browser.close()

#=====================================================================================


# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.saucedemo.com/")

#     username = page.locator("#user-name")      # Locators
#     password = page.locator("#password")
#     login_button = page.locator("#login-button")

#     # Print locators
#     print("Username Placeholder:", username.get_attribute("placeholder"))
#     print("Password Placeholder:", password.get_attribute("placeholder"))
#     print("Login Button Text:", login_button.get_attribute("value"))

#     page.wait_for_timeout(3000)  
#     browser.close()

#=====================================================================================


# from playwright.sync_api import sync_playwright


# def successful_login(page):
#     page.goto("https://www.saucedemo.com/")
#     page.locator("#user-name").fill("standard_user")
#     page.locator("#password").fill("secret_sauce")
#     page.wait_for_timeout(2000)
#     page.locator("#login-button").click()

#     page.wait_for_url("**/inventory.html")
#     assert "inventory.html" in page.url
#     print("✅ Success Login Passed")
    


# def invalid_login(page):
#     page.goto("https://www.saucedemo.com/")
#     page.locator("#user-name").fill("wrong_user")
#     page.locator("#password").fill("wrong_pass")
#     page.locator("#login-button").click()

#     error = page.locator("[data-test='error']").text_content()
#     print("Error:", error)

#     assert "Username and password do not match" in error
#     print("✅ Error Scenario Passed")
#     page.wait_for_timeout(2000)


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()

#     successful_login(page)
#     page.wait_for_timeout(3000)
#     invalid_login(page)
    
#     browser.close()
#=====================================================================================


# from playwright.sync_api import expect, sync_playwright

# def successful_login(page):
#     page.locator("#user-name").fill("standard_user")
#     page.locator("#password").fill("secret_sauce")
#     page.wait_for_timeout(1000)
#     page.locator("#login-button").click()

#     page.wait_for_url("**/inventory.html")
#     assert "inventory.html" in page.url
#     inventory_locator = page.locator(".inventory_container")
#     expect(inventory_locator).to_be_visible()

#     # Verify product count >= 6
#     inventory_count = page.locator(".inventory_item").count()
#     assert inventory_count >= 6, f"Expected at least 6 products, but found {inventory_count}"

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://www.saucedemo.com/")
#     # Verify title
#     expect(page).to_have_title("Swag Labs")
#     successful_login(page)
#     page.wait_for_timeout(2000)

#     # Verify inventory container is visible
#     inventory_locator = page.locator(".inventory_container")
#     inventory_count = page.locator(".inventory_item").count()
#     if inventory_count >= 6:
#         print("Inventory has total items:", inventory_count)
#     else:
#         print("Inventory has less than 6 items:", inventory_count)
    
#=====================================================================================
# cart
from playwright.sync_api import Page, expect, sync_playwright

def successful_login(page):
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.wait_for_timeout(1000)
    page.locator("#login-button").click()

# sort products
def test_sort_products(page):
    page.locator(".product_sort_container").select_option("lohi")
    
def test_add_items_to_cart(page: Page):
    
    add_to_cart_button = page.get_by_role("button", name="Add to cart")
    button_count = add_to_cart_button.count()
    print(f"Found {button_count} buttons")

# Loop through a fixed number of items (e.g., first 3 items)
    for i in range(3):
        # Use .nth(i) to safely target each item sequentially
        add_to_cart_button.nth(i).click()

# 4. Verify the cart icon badge displays "3"
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("3")
    
def test_cart_checkout(page: Page):
    page.locator(".shopping_cart_link").click()
    page.wait_for_timeout(2000)
    checkout_button = page.get_by_role("button", name="Checkout")
    checkout_button.click()
    page.wait_for_timeout(2000)
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    # Verify title
    expect(page).to_have_title("Swag Labs")
    successful_login(page)
    test_sort_products(page)
    test_add_items_to_cart(page)
    page.wait_for_timeout(1000)
    test_cart_checkout(page)


