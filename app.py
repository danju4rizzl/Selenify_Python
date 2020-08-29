from selenium import webdriver

browser = webdriver.Chrome()

url = "https://github.com"
username = "**** YOUR GITHUB USERNAME*****"
user_password = "**** YOUR GITHUB PASSWORD  ****"

browser.get(url)

sign_in = browser.find_element_by_link_text("Sign in")
sign_in.click()

username_input = browser.find_element_by_id("login_field")
username_input.send_keys(username)

password_input = browser.find_element_by_id("password")
password_input.send_keys(user_password)
password_input.submit()

profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")

if password_input.submit:
    assert username in link_label
    browser.quit()
    print("WOOWHOOO 🔥")
else:
    browser.close()
