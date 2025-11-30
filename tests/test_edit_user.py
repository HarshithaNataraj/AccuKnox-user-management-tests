import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_edit_user(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.navigate()
    login.login("admin", "BS3Om@y2Zf")
    page.get_by_text("HR Administration").wait_for(state="visible", timeout=20000)
    

def test_admin_edit_username(page):
    admin = AdminPage(page)

    admin.open_user("harshi_test")
    admin.edit_username("bindu@845")
    admin.save()

    assert page.get_by_text("bindu@845").is_visible()

def test_admin_edit_role(page):
    admin = AdminPage(page)

    admin.open_user("bindu@845")
    admin.edit_admin_role("Report Admin")
    admin.save()

    assert page.get_by_text("Report Admin").is_visible()


def test_admin_modify_region(page):
    admin = AdminPage(page)

    admin.open_user("bindu@845")
    admin.edit_region("Canada")
    admin.save()

    assert page.get_by_text("Canada").is_visible()


def test_admin_update_status(page):
    admin = AdminPage(page)

    admin.open_user("bindu@845")
    admin.set_status_enabled()
    admin.save()

    assert page.get_by_text("Enabled").is_visible()

def test_admin_edit_password(page):
    admin = AdminPage(page)

    admin.open_user("bindu@845")
    admin.edit_password("Management")
    admin.save()

    assert page.get_by_text("Password updated successfully").is_visible()

def test_admin_cancel_edit(page):
    admin = AdminPage(page)

    admin.open_user("bindu@845")
    admin.edit_username("user_not_saved")
    admin.cancel()

    assert not page.locator("text=user_not_saved").is_visible()
