from playwright.sync_api import Playwright, expect, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://ais.usvisa-info.com/en-ca/niv/users/sign_in")
    page.get_by_label("Email *").click()
    page.get_by_label("Email *").fill("maian@gmail.com")
    page.get_by_label("Email *").press("Tab")
    page.get_by_label("Password").fill("lsivnlrsv")
    page.locator("label").filter(
        has_text="I have read and understood the Privacy Policy and the Terms of Use"
    ).locator("div").click()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_label("Email").click()
    page.locator("label").filter(
        has_text="I have read and understood the Privacy Policy and the Terms of Use"
    ).locator("div").click()
    page.locator("label").filter(
        has_text="I have read and understood the Privacy Policy and the Terms of Use"
    ).locator("div").click()
    page.get_by_label("Email").click()
    page.get_by_label("Email").fill("shashinpatel251@gmail.com")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill("Nayosha*1999")
    page.locator("label").filter(
        has_text="I have read and understood the Privacy Policy and the Terms of Use"
    ).locator("div").click()
    page.locator("label").filter(
        has_text="I have read and understood the Privacy Policy and the Terms of Use"
    ).locator("div").click()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("link", name="Continue").click()
    page.get_by_role("tab", name=" Reschedule Appointment").click()
    page.get_by_role("link", name="Reschedule Appointment").click()
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "94"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "92"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "95"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "90"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "93"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "91"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "90"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "94"
    )
    page.get_by_text(
        "There are no available appointments at the selected location. Please try again l"
    ).click()
    page.get_by_text(
        "There are no available appointments at the selected location. Please try again l"
    ).click()
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "92"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "91"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "90"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "89"
    )
    page.get_by_role("combobox", name="Consular Section Location\n*").select_option(
        "95"
    )
    page.get_by_role("link", name="Close").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
