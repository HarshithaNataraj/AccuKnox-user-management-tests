
# AccuKnox User Management Automation – OrangeHRM (Python + pytest)

## 🎯 Objective
Automate the User Management workflow on the OrangeHRM  site using Playwright (Python).

## ⚙️ Project Setup Steps

1. Install Python 3.11.9
   - Check: `python --version`

2. Clone the Repository
   ```bash
   git clone https://github.com/<your-username>/AccuKnox-user-management-tests.git
   cd AccuKnox-user-management-tests
   ```

3. Create Virtual Environment
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux
   ```

4. Install Dependencies
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## ▶️ How to Run the Test Cases


1. Run a specific test file:
   ```bash
   pytest tests/test_navigate.py --headed 
   ```

## 🧩 Playwright Version Used
Playwright **v1.56.0.** (documented here; use latest if preferred)

## 🗂️ Folder Structure
```
AccuKnox-user-management-tests/
├── pages/
│   ├── login_page.py
│   └── admin_page.py
├── tests/
    ├── test_navigate.py
│   ├── test_add_user.py
│   ├── test_search_user.py
│   ├── test_edit_user.py
│   ├── test_validate_user.py
│   ├── test_delete_user.py
    
      
├── conftest.py
├── requirements.txt
├── README.md
└── AccuKnox_User_Management_TestCases.xlsx
```

## 🪲 Notes / Known Issues
- The Employee Name field is read-only after user creation. Automated tests cannot edit this field; scripts should only verify its value.
- The public OrangeHRM demo site occasionally displays SSL certificate warnings (ERR_CERT_COMMON_NAME_INVALID).  
Due to this, authentication and navigation may not work reliably in automation.

To avoid instability, this project uses the  OrangeHRM cloud trial instance instead of the public demo environment.

## 👩‍💻 Author
Harshitha S N
