from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_admin_menu_visible(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.navigate()
    login.login('admin', 'BS3Om@y2Zf')

    assert admin.is_hr_admin_menu_visible() == True

def test_admin_page_loaded(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.navigate()
    login.login('admin', 'BS3Om@y2Zf')

    admin.open_admin()
    assert admin.is_page_loaded() == True

def test_open_admin_module(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.navigate()
    login.login('admin', 'BS3Om@y2Zf')
    
    admin.open_admin()  
    assert admin.is_page_loaded() == True

def test_admin_ui_elements(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.navigate()
    login.login('admin', 'BS3Om@y2Zf')

    admin.open_admin()
    assert admin.ui_elements_available() == True

def test_non_admin_cannot_access_admin(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.navigate()
    login.login('Employee01', 'emp@123')  # Non-admin user

    # Attempt to open admin module
    admin.open_admin()

    # Admin page should not load
    expect(page.get_by_text("Invalid Credentials")).to_be_visible()