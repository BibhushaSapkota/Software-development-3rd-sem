import imp
from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pythonBDD.Utilities.customLogger import LogGen
from pythonBDD.Utilities.readproperty import ReadConfig

baseURL=ReadConfig.getURL()
mylogger=LogGen.loggen()

@given('Launch the browser')
def stepl_impl(context):
    context.driver=webdriver.Chrome(ChromeDriverManager().install)
    mylogger.info("****Driver Installed*******")
    context.driver.get(baseURL)
    mylogger.info("Browser lauched")

@then('verify the page title')
def step_imp(context):
    actual_title=context.driver.title
    print(actual_title)
    expected_title= "Chhatrabas"

    if actual_title==expected_title:
        assert True 
        mylogger.info("****Title matched*****")

    else:
        mylogger.info("****Title not matched*****")
        assert False

@then('close the browser')
def step_impl(context):
    context.driver.close()
    mylogger.info('*****Browser closed')
