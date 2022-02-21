from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given(u'Launch Chrome Browser')
def open_browser(context):
    context.driver= webdriver.Chrome(ChromeDriverManager().install())


@when(u'Open ChhatraBas Homepage')
def openHome(context):
    context.driver.get("http://127.0.0.1:8000/")


@then(u'Verify that the logo is present on webpage')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("/html/body/div/div/nav/a[2]").is_displayed()
    assert status is True
@then(u'Close Browser')
def closeBrowser(context):
    context.driver.close()