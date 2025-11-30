import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.admin_page import AdminPage


def test_delete_user(page: Page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.navigate()
    login.login("admin", "BS3Om@y2Zf")
    page.get_by_text("HR Administration").wait_for(state="visible", timeout=20000)
    
    username = "bindu@845"
    
    
    # 1. Verify Admin can select a user to delete
    admin.select_user(username)
    
    # 2. Verify Admin able to click on Delete via three horizontal dots
    admin.click_delete_from_dots()
    
    # 3. Verify Admin should be able to see confirmation popup
    assert admin.confirm_popup.is_visible()
    
    # 4. Verify Admin can cancel the delete action
    admin.cancel_delete()
    assert admin.is_user_present(username)
    
    # 5. Verify Admin can confirm and delete a user
    admin.select_user(username)
    admin.click_delete_from_dots()
    admin.confirm_delete()
    
    # 6. Verify Admin should be able to view success message
    assert admin.is_success_message_visible()
    
    # 7. Verify Admin should not be able to delete non-selected users
    admin.click_delete_from_dots()  # without selecting a user
    assert not admin.confirm_popup.is_visible()
    
    # 8. Verify Admin not able to get the deleted user
    assert not admin.is_user_present(username)
