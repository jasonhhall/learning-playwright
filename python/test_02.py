import pytest
from playwright.sync_api import Page, Playwright, sync_playwright, expect

def practice_form(page: Page):
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("QA")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("textbox", name="Last Name").fill("Tester")
    page.get_by_role("textbox", name="name@example.com").click()
    page.get_by_role("textbox", name="name@example.com").fill("test@test.com")
    page.get_by_text("Other").click()
    page.get_by_role("textbox", name="Mobile Number").click()
    page.get_by_role("textbox", name="Mobile Number").fill("9")
    page.get_by_role("textbox", name="Mobile Number").click()
    page.get_by_role("textbox", name="Mobile Number").fill("1234567890")
    page.locator("#dateOfBirthInput").click()
    page.get_by_role("combobox").nth(1).select_option("2000")
    page.locator("#state svg").click()
    page.get_by_text("NCR", exact=True).click()
    page.locator("#city svg").click()
    page.get_by_text("Delhi", exact=True).click()
    page.get_by_role("button", name="Submit").click()
    
def run(playwright: Playwright):
    firefox = playwright.firefox
    browser = firefox.launch(headless=False)
    page = browser.new_page()
    url = "https://demoqa.com/automation-practice-form"
    page.goto(url)
    practice_form(page)
    expect(page.locator("#example-modal-sizes-title-lg")).to_contain_text("Thanks for submitting the form")
#  page.pause()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)