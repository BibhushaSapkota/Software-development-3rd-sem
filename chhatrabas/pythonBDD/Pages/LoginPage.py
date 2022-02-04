class LoginPage:
    txt_username_id="inputusername"
    txt_password_id="inputPassword"
    btn_login_xpath="/html/body/div/form/div[2]/div/input"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element_by_id(self.txt_username_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element_by_id(self.txt_password_id_id).send_keys(password)

    def clickOnLogin(self):
        self.driver.find_element_by_id(self.btn_login_xpath).click()