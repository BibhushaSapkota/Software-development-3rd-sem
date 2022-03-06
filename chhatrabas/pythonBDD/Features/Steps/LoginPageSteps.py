from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pythonBDD.Utilities.customLogger import LogGen
from pythonBDD.Utilities.readproperty import ReadConfig
from pythonBDD.Pages import HomePage,LoginPage
import time

baseURL=ReadConfig.getURL()
mylogger=LogGen.loggen()

@given(u'Launch the app')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    mylogger.info("****Driver Installed*******")
    context.driver.get(baseURL)
    mylogger.info("****Browser lauched****")



@when(u'enter login credentials')
def step_impl(context):
    mylogger.info("****Passing Credentials****")
    global homepage
    global loginpage
    homepage=HomePage(context.driver)
    homepage.clickOnLogin()
    loginpage= LoginPage()
    user = ReadConfig.getUserName()
    pwd = ReadConfig.getPassword()
    time.sleep(3)

    loginpage.setusername(user)
    loginpage.setpassword(pwd)
    mylogger.info("****Entered credential****")


@then(u'click login')
def step_impl(context):
    loginpage.clickOnLogin()
    mylogger.info("****Login Button Clicked****")



@then(u'close the App')
def step_impl(context):
    context.driver.close()
    mylogger.info('*****Browser closed')
