import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.admin_page import AdminPage



@pytest.fixture
def admin_page(page: Page): 
    page.goto("https://sinchu-trials719.orangehrmlive.com/auth/seamlessLogin")
    login = LoginPage(page)
    login.login("admin", "BS3Om@y2Zf")
    page.get_by_text("HR Administration").wait_for(state="visible", timeout=20000)
    return AdminPage(page)

    


def test_navigate_to_add_user(admin_page: AdminPage):
    admin_page.page.get_by_text("Add User").click()
    admin_page.page.get_by_text("Add User").wait_for(state="visible", timeout=10000)
    assert "Add User" in admin_page.page.content()


def test_add_user_valid_details(admin_page: AdminPage):
    admin_page.page.get_by_text("Add User").click()
    admin_page.employee_name_input.fill("Jenny Fisher")
    admin_page.username_field.fill("harshi_test")
    admin_page.password_field.fill("Test@123")
    admin_page.confirm_password_field.fill("Test@123")

    admin_page.select_admin_role("Global Admin")
    admin_page.select_ess_role("Default ESS")
    admin_page.select_supervisor_role("Default Supervisor")
    admin_page.select_status_enabled()
    admin_page.click_save()
    assert admin_page.page.get_by_text("harshi_test").is_visible()


def test_add_user_duplicate_username(admin_page: AdminPage):
    admin_page.page.get_by_text("Add User").click()
    admin_page.employee_name_input.fill("Jenny Fisher")
    admin_page.username_field.fill("harshi_test")
    admin_page.password_field.fill("Test@123")
    admin_page.confirm_password_field.fill("Test@123")
    admin_page.select_admin_role("Global Admin")
    admin_page.select_ess_role("Default ESS")
    admin_page.select_supervisor_role("Default Supervisor")
    admin_page.select_status_enabled()
    admin_page.click_save()
    # Verify duplicate username error
    assert admin_page.page.get_by_text("Username Already exists").is_visible()


def test_add_user_mandatory_fields_empty(admin_page: AdminPage):
    admin_page.page.get_by_text("Add User").click()
    admin_page.click_save()
    # Verify mandatory field errors
    assert admin_page.page.get_by_text("Required").is_visible()


def test_password_mismatch(admin_page: AdminPage):
    admin_page.page.get_by_text("Add User").click()
    admin_page.employee_name_input.fill("Jenny Fisher")
    admin_page.username_field.fill("harshi_test")
    admin_page.password_field.fill("Test@123")
    admin_page.confirm_password_field.fill("Test@124")
    admin_page.select_admin_role("Global Admin")
    admin_page.select_ess_role("Default ESS")
    admin_page.select_supervisor_role("Default Supervisor")
    admin_page.select_status_enabled()
    admin_page.click_save()
    # Verify password mismatch error
    assert admin_page.page.get_by_text("Passwords do not match").is_visible()


def test_invalid_password_format(admin_page: AdminPage):
    admin_page.page.get_by_text("Add User").click()
    admin_page.employee_name_input.fill("Jenny Fisher")
    admin_page.username_field.fill("harshi_test")
    admin_page.password_field.fill("456")
    admin_page.confirm_password_field.fill("456")
    admin_page.select_admin_role("Global Admin")
    admin_page.select_ess_role("Default ESS")
    admin_page.select_supervisor_role("Default Supervisor")
    admin_page.select_status_enabled()
    admin_page.click_save()
    # Verify invalid password format error
    assert admin_page.page.get_by_text("Invalid password format").is_visible()


def test_disabled_user_creation(admin_page: AdminPage):
    admin_page.page.get_by_text("Add User").click()
    admin_page.employee_name_input.fill("Jenny Fisher")
    admin_page.username_field.fill("harshi_test")
    admin_page.password_field.fill("Test@123")
    admin_page.confirm_password_field.fill("Test@123")
    admin_page.select_admin_role("Global Admin")
    admin_page.select_ess_role("Default ESS")
    admin_page.select_supervisor_role("Default Supervisor")
    admin_page.select_status_disabled()
    admin_page.click_save()
    # Verify user is disabled
    assert admin_page.page.get_by_text("harshi_test").is_visible()
    assert admin_page.page.get_by_text("Disabled").is_visible()


def test_mandatory_role_selection(admin_page: AdminPage):
    admin_page.page.get_by_text("Add User").click()
    admin_page.employee_name_input.fill("Jenny Fisher")
    admin_page.username_field.fill("harshi_test")
    admin_page.password_field.fill("Test@123")
    admin_page.confirm_password_field.fill("Test@123")    
    # Do not select roles
    admin_page.click_save()
    # Verify error messages for roles
    assert admin_page.page.get_by_text("Required").is_visible()
    assert admin_page.page.get_by_text("Required").is_visible()


def test_user_visible_after_creation(admin_page: AdminPage):
    admin_page.page.get_by_text("Add User").click()
    admin_page.employee_name_input.fill("Jenny Fisher")
    admin_page.username_field.fill("harshi_test")
    admin_page.password_field.fill("Test@123")
    admin_page.confirm_password_field.fill("Test@123")
    admin_page.select_admin_role("Global Admin")
    admin_page.select_ess_role("DEfault ESS")
    admin_page.select_supervisor_role("Default Supervisor")
    admin_page.select_status_enabled()
    admin_page.click_save()
    # Verify new user visible in list
    assert admin_page.page.get_by_text("harshi_test").is_visible()


def test_cancel_button_functionality(admin_page: AdminPage):
    admin_page.page.get_by_text("Add User").click()
    admin_page.employee_name_input.fill("Jenny Fisher")
    admin_page.username_field.fill("harshi_test")
    admin_page.password_field.fill("Test@123")
    admin_page.confirm_password_field.fill("Test@123")
    admin_page.click_cancel()
    # Verify Add User form closed
    assert not admin_page.username_field.is_visible()
    