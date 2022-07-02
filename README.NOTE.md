# Search
    https://github.com/mathare
    pytest bdd selenium website github

# Chrome
Lựa chọn phiên bản Chrome

    chrome://settings/help
    https://www.selenium.dev/downloads/
    https://chromedriver.chromium.org/

Trong conftest.py có hai lựa chọn cho webdriver.Chrome 

    Invisible: webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    Visible: webdriver.Chrome(executable_path=r'C:/Users/{name}/{project}/chromedriver_win32/chromedriver.exe')

# Cài đặt các phần mềm
    pip install -r requirements

# Pytest-BDD
features: 

    Scenario: Truyền giá trị "value"
    Scenario Outline: Truyền biến <variable> 
    Scenario Outline: Truyền biến "<variable>"

step_defs: 

    Nhận giá trị "{param}"
    Nhận biến {param}
    Nhận biến "{param}"