from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@given('el navegador está abierto')
def step_open_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

@when('navego a "{url}"')
def step_navigate_to(context, url):
    context.driver.get(url)

@then('el título de la página debería ser "{expected_title}"')
def step_check_title(context, expected_title):
    actual_title = context.driver.title
    assert actual_title == expected_title, f"Expected title to be '{expected_title}' but got '{actual_title}'"
    context.driver.quit()
