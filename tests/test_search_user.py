import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_search_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.navigate()
    login.login("admin", "BS3Om@y2Zf")
    page.get_by_text("HR Administration").wait_for(state="visible", timeout=20000)
 



def test_search_user_by_username(admin_page):
    admin_page.click_filter()
    admin_page.set_username_filter("harshi_test")
    admin_page.click_search()

    assert admin_page.page.get_by_text("rshi_test").is_visible()

def test_search_user_by_employee_name(admin_page):
    admin_page.click_filter()
    admin_page.set_employee_name_filter("Jenny Fisher")
    admin_page.click_search()

    assert admin_page.page.get_by_text("John Doe").is_visible()

def test_search_user_by_status_enabled(admin_page):
    admin_page.click_filter()
    admin_page.select_status("Enabled")
    admin_page.click_search()

    assert admin_page.page.get_by_text("Enabled").first.is_visible()

def test_search_user_by_status_disabled(admin_page):
    admin_page.click_filter()
    admin_page.select_status("Disabled")
    admin_page.click_search()

    assert admin_page.page.get_by_text("Disabled").first.is_visible()

def test_search_user_by_ess_and_supervisor(admin_page):
    admin_page.click_filter()
    admin_page.select_ess_role("Default ESS")
    admin_page.select_supervisor_role("Default Supervisor")
    admin_page.click_search()

    assert admin_page.page.get_by_text("Default ESS").first.is_visible()
    assert admin_page.page.get_by_text("DEfault Supervisor").first.is_visible()

def test_search_user_by_admin_role(admin_page):
    admin_page.click_filter()
    admin_page.select_admin_role("Global Admin")
    admin_page.click_search()

    assert admin_page.page.get_by_text("Admin").first.is_visible()

def test_filter_reset(admin_page):
    admin_page.click_filter()
    admin_page.set_username_filter("harshi_test")
    admin_page.click_search()

    admin_page.click_filter()
    admin_page.click_reset()

    assert admin_page.username_filter.input_value() == ""

def test_search_by_username_and_role(admin_page):
    admin_page.click_filter()
    admin_page.set_username_filter("harshi_test")
    admin_page.select_admin_role("test@123")
    admin_page.click_search()

    assert admin_page.page.get_by_text("harshi_test").is_visible()
    assert admin_page.page.get_by_text("test@123").is_visible()

def test_cancel_filter(admin_page):
    admin_page.click_filter()
    admin_page.set_username_filter("harshi_test")
    admin_page.click_cancel()

    assert not admin_page.username_filter.is_visible()
