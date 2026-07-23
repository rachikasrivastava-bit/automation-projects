from playwright.sync_api import Page

class SortAddCart:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = page.locator(".shopping_cart_link")
        self.sort_items = page.locator(".product_sort_container")
        self.checkout_button = page.locator("[data-test='checkout']")

    def sort_and_add_to_cart(self):
        self.sort_items.select_option("lohi")

        add_to_cart_buttons = self.page.get_by_role("button", name="Add to cart")
        count = add_to_cart_buttons.count()
        for i in range(min(3, count)):
            add_to_cart_buttons.nth(i).click()

    def go_to_cart(self):
        self.cart_icon.click()

    def proceed_to_checkout(self):
        self.checkout_button.click()
    