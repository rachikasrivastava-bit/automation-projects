import pytest

from playwright.sync_api import expect

# Simply pass the fixture names from conftest.py as arguments
# def test_verify_dashboard_message(login_session):
    
#     # app_logo = login_session.locator(".header_label")
    
#     # assert app_logo.text_content() == "Swag Labs"

#     expect(login_session.locator(".header_label")).to_have_text("Swag Labs")

def test_verify_dashboard_message(login_session):
    login_session.wait_for_selector(".app_logo", timeout=5000)
    expect(login_session.locator(".app_logo")).to_have_text("Swag Labs")
