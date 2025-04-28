from selenium import webdriver
from base.basedriver import Basedriver


def before_all(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://automationexercise.com/")
    context.base = Basedriver(context.driver)
    
def after_all(context):
    context.driver.quit()    