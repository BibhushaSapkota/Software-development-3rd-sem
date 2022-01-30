from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from pythonBDD.Utilities.customLogger import LogGen
from pythonBDD.Utilities.readproperty import ReadConfig


@given(u'Launch the app')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Launch the app')


@when(u'enter login credentials')
def step_impl(context):
    raise NotImplementedError(u'STEP: When enter login credentials')


@then(u'click login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then click login')


@then(u'close the App')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then close the App')
