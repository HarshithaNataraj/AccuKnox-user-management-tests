import pytest
from pages.admin_page import AdminPage
from pages.login_page import LoginPage  

def test_user_validations(page):
    login = LoginPage(page)
    admin = AdminPage(page)

    login.navigate()
    login.login("admin", "BS3Om@y2Zf")

    
    admin.update_username("bindu@845")
    admin.save_user()
    admin.search_user("bindu@123")
    assert page.get_by_text("bindu@845").is_visible()

    
    admin.update_ESS(" ")
    # Don't select ESS role
    assert admin.is_error_displayed("Required")

    admin.update_ESS(" ")
    # Don't select supervisor role
    assert admin.is_error_displayed("Required")

    # 3. Employee name not editable
    # employee_name_input is readonly after creation
    assert admin.is_employee_field_disabled(), "Employee field should be read-only after creation"


    admin.edit_admin_role("Report Admin")
    admin.save()
    assert page.get_by_text("Report Admin").is_visible()

   
    admin.select_status("Enabled")
    admin.save_user()
    assert not admin.is_error_displayed("Status is required")

  
    admin.select_region("Canada")
    admin.save_user()
    assert page.get_by_text("Canada").is_visible()

  
    admin.update_username("mbindu@845")
    admin.select_ess_role("Default ESS")
    admin.select_supervisor_role("Default Supervisor")
    admin.select_admin_role("Report Admin")
    admin.select_status("Enabled")
    admin.select_region("Canada")
    admin.save_user()
   
