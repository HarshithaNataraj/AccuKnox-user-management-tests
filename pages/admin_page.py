import pytest
from playwright.sync_api import Page, expect

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        # navigation
        self.admin_menu = page.get_by_role("link", name="HR Administration")

        # Page header
        self.header_text = page.get_by_role("heading", name="HR Administration")
        
        #  UI elements 
        #self.user_table = page.locator("[data-automation-id='menu_admin_viewSystemUsers']")
        self.user_table = page.get_by_role("link", name="Users")  
        self.add_user_btn = page.get_by_role("button", name="Add User")
        self.header_text = page.get_by_role("heading", name="Admin")

    def open_admin(self):
        self.admin_menu.click()
        expect(self.header_text).to_be_visible(timeout=15000)

    def is_admin_menu_visible(self):
        return self.admin_menu.is_visible()

    def is_page_loaded(self):
        return self.header_text.is_visible()

    def ui_elements_available(self):
        return (
            self.user_table.is_visible()  and
            self.add_user_btn.is_visible() 
        )

    def test_non_admin_unauthorized_error(page, login_as_non_admin):
        page.goto("/admin/systemUsers")
        expect(page.get_by_text("Invalid Credentials")).to_be_visible()

    
    



 # add user  - placeholders used where possible
        self.employee_name_input = page.locator("input[placeholder='Type for hints...']")
        self.username_field = page.locator("[id='user_name']")
        self.status_field = page.locator("div[role='listbox']").first
        self.password_field = page.locator("input[type='password']").nth(0)
        self.confirm_password_field = page.locator("input[type='confirmpassword']").nth(1)
        self.save_btn = page.get_by_role("button", name="Save")
        self.cancel_btn = page.get_by_role("button", name="Cancel")

    def select_admin_role(self, role_name: str = "Admin"):
        page.locator("input.dropdown-field-focus-element")
        self.admin_role_dropdown.click()
        self.page.get_by_text(role_name, exact=True).click()

    def select_ess_role(page, role_name):
        page.locator("input.dropdown-field-focus-element").click()
        self.ess_role_dropdown.click()
        page.get_by_text("Default ESS", exact=True).click()

    def select_supervisor_role(self, option: str):
        self.supervisor_role_dropdown = page.locator("input.placeholder.dropdown-field-focus-element[readonly][value='Default Supervisor']")
        self.supervisor_role_dropdown.click()
        page.get_by_text("Default Supervisor", exact=True).click()

    def select_status_enabled(self):
        self.page.locator("label[for='status_1']").click()

    def select_status_disabled(self):
        self.page.locator("label[for='status_2']").click()





  # search the users by filters
        self.username_filter = page.locator("input#systemuser_name_filter")  
        self.employee_name_filter = page.locator("input#employee_name_filter_value[placeholder='Type for hints...']")  
        self.ess_role_dropdown = page.locator("input.select-dropdown[placeholder='ESS Role'], input.select-dropdown[value='Default ESS']").nth(0)
        self.supervisor_role_dropdown = page.locator("input.select-dropdown[placeholder='Supervisor Role'], input.select-dropdown[value='Default Supervisor']").nth(2)
        self.status_dropdown = page.locator("input.select-dropdown[placeholder='Status'], input.select-dropdown[value='Enabled']").nth(0)
        self.status_dropdown = page.locator("input.select-dropdown[placeholder='Status'], input.select-dropdown[value='Disabled']").nth(1)
        self.location_dropdown = page.locator("input.select-dropdown[placeholder='Location'], input.select-dropdown[value='India']")
        self.reset_btn = page.locator("a.modal-action.modal-close:has-text('Reset')")
        self.cancel_btn = page.locator("a.modal-action.modal-close:has-text('Cancel')")
        self.search_btn = page.locator("a.modal-action.modal-close.primary-btn:has-text('Search')")

        
    def click_filter(self):
        self.filter_btn = page.locator("a[data-tooltip='Filter']")  # Filter button
        self.filter_btn.click()

    def select_admin_role(self, role_name: str):
        page.locator("input.dropdown-field-focus-element")
        self.admin_role_dropdown.click()
        self.page.get_by_text(role_name, exact=True).click()

    def select_ess_role(page, role_name):
        page.locator("input.dropdown-field-focus-element").click()
        self.ess_role_dropdown.click()
        page.get_by_text("Default ESS", exact=True).click()

    def select_supervisor_role(self, option: str):
        self.supervisor_role_dropdown = page.locator("input.placeholder.dropdown-field-focus-element[readonly][value='Default Supervisor']")
        self.supervisor_role_dropdown.click()
        page.get_by_text("Default Supervisor", exact=True).click()


#Edit user details 

 
        self.username_input = page.locator("input#user_name")
        self.supervisor_role_dropdown = page.locator("input[value='Default Supervisor']")
        self.status_enabled_radio = page.locator("label[for='status_1']")
        self.change_password_checkbox = page.locator("label[for='changepassword']")
        self.password_field = page.locator("input[type='password']").nth(0)
        self.confirm_password_field = page.locator("input[type='confirmpassword']").nth(1)
        self.cancel_button = page.locator("button.btn.btn-ghost")
        self.save_button = page.locator("button#modal-save-button")
 
    def open_user(self, username):
        self.page.locator(f"//div[text()='{username}']").click()

    def edit_username(self, new_username):
        self.username_input.fill(new_username)

    def edit_admin_role(self, role_name):
        page.locator("input.dropdown-field-focus-element")
        self.admin_role_dropdown.click()
        self.page.locator(f"//span[normalize-space()='{role_name}']").click()

    def edit_region(self, region_name):
        self.region_dropdown.click()
        self.page.locator(f"//span[normalize-space()='{region_name}']").click()

    def set_status_enabled(self):
        self.status_enabled_label.click()

    def edit_password(self, new_pass):
        self.password_checkbox.click()
        self.password_input.fill(new_pass)
        self.confirm_password_input.fill(new_pass)

    def save(self):
        self.save_button.click()

    def cancel(self):
        self.cancel_button.click()

# delete user 
        self.user_checkbox = page.locator("label[for='checkbox_list0_8']")
        self.more_actions_icon = page.locator("i.material-icons", has_text="more_horiz")
        self.delete_selected_option = page.locator("a", has_text="Delete Selected")
        self.confirm_cancel_btn = page.locator("button", has_text="No, Cancel")
        self.confirm_delete_btn = page.locator("button#save-button", has_text="Yes, Delete")

        # Actions
    def select_user(self):
        self.user_checkbox.click()

    def open_more_actions(self):
        self.more_actions_icon.click()

    def click_delete_selected(self):
        self.delete_selected_option.click()

    def confirm_delete(self):
        self.confirm_delete_btn.click()

    def cancel_delete(self):
        self.confirm_cancel_btn.click()

#validate 

        self.username_input = page.locator("#user_name")
        self.employee_input = page.locator("input[id='selectedEmployee_value']")
        self.supervisor_role_dropdown = page.get_by_text("Supervisor Role").locator("xpath=..").locator("div[role='combobox']")
        self.status_dropdown = page.get_by_text("Status").locator("xpath=..").locator("div[role='combobox']")
        self.region_dropdown = page.get_by_text("Region").locator("xpath=..").locator("div[role='combobox']")
        self.save_btn = page.get_by_role("button", name="Save")
        self.error_message = page.locator(".error-message")  # generic locator for validation messages

    # Actions
    def update_username(self, username: str):
        self.username_input.fill(username)

    def is_employee_field_disabled(self) -> bool:
        return self.employee_input.is_disabled() or self.employee_input.get_attribute("readonly") is not None
    
    def select_ess_role(self, role: str):
        page.locator("input.dropdown-field-focus-element").click()
        self.ess_role_dropdown.click()
        self.page.get_by_text(role, exact=True).click()

    def select_supervisor_role(self, role: str):
        self.supervisor_role_dropdown = page.locator("input.placeholder.dropdown-field-focus-element[readonly][value='Default Supervisor']")
        self.supervisor_role_dropdown.click()
        self.page.get_by_text(role, exact=True).click()

    def select_admin_role(self, role: str):
        page.locator("input.dropdown-field-focus-element")
        self.admin_role_dropdown.click()
        self.page.get_by_text(role, exact=True).click()

    def select_status(self, status: str):
        self.status_dropdown.click()
        self.page.get_by_text(status, exact=True).click()

    def select_region(self, region: str):
        self.region_dropdown.click()
        self.page.get_by_text(region, exact=True).click()

    def save_user(self):
        self.save_btn.click()

    
    def get_field_value(self, locator):
        return locator.input_value()





 