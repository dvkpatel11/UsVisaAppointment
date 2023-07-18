# Aksharam Aham Purushottam Dashoshmi
import re
import time
from datetime import datetime, timedelta
from pathlib import Path

from dateutil import parser
from playwright.sync_api import TimeoutError, sync_playwright

from creds import appointment_id, appointment_url, password, user, visa_locations

cur_date = None
login_url = "https://ais.usvisa-info.com/en-ca/niv/users/sign_in"
username_id = "Email"
password_id = "Password"
terms_id = "I have read and understood the Privacy Policy and the Terms of Use"
sign_in_id = "Sign In"
appointment_link = (
    appointment_url
    if appointment_url
    else "https://ais.usvisa-info.com/en-ca/niv/schedule/{}/appointment"
)
continue_id = "Continue"
location_id = "#appointments_consulate_appointment_facility_id"
not_available_id = "#consulate_date_time_not_available"
locations = [
    "Calgary",
    "Halifax",
    "Montreal",
    "Ottawa",
    "Quebec City",
    "Toronto",
    "Vancouver",
]
calender_dropdown_date_id = "#appointments_consulate_appointment_date"
next_link = "Next"
a_elements = "//a[@href]"
appointment_date_id = ".consular-appt"
appointment_date_regex = r".*Appointment:(.*)Vancouver local time.*$"
date_of_appointment_id = "#appointments_consulate_appointment_date"
calender_id = ".ui-datepicker-title"
datepicker_calendar_id = "#ui-datepicker-calendar"
found_date = None
address_id = "#appointments_consulate_availability"
calender_month_id = ".ui-datepicker-month"
calender_year_id = ".ui-datepicker-year"


def month_to_num(m):
    return {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }[m]


class VisaAutomate:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.ind = 0
        self.folder = str(int(time.time()))
        Path(f"./screenshots/{self.folder}").mkdir(parents=True, exist_ok=True)

    def go_to_page(self, page):
        self.page.goto(page)

    def screenshot(self, name: str = "image"):
        self.page.screenshot(path=f"./screenshots/{self.folder}/{name}-{self.ind}.png")
        self.ind = self.ind + 1

    def login(self, username, passwd, cont=True):
        self.go_to_page(login_url)
        self.page.get_by_label(username_id).fill(username)
        self.page.get_by_label(password_id).fill(passwd)
        self.page.locator("label").filter(has_text=terms_id).click()
        self.page.get_by_role("button", name=sign_in_id).click()
        self.screenshot("logged-in")
        if cont:
            self.page.get_by_role("menuitem", name=continue_id).click()

    def go_to_appointments(self, appoint_id):
        self.page.goto(appointment_link.format(appoint_id))
        self.page.wait_for_load_state("networkidle")

    def check_availability(self, cur_date):
        global found_date
        self.page.locator(calender_id).first.text_content()

        td_elements = self.page.query_selector_all("td")
        for td_element in td_elements:
            # get date
            href_value = td_element.get_attribute("href")
            if href_value:
                # Found the link
                try:
                    day = int(td_element.text_content())
                    month = int(td_element.get_attribute("data-month"))
                    year = int(td_element.get_attribute("data-year"))
                    print(
                        f' day {td_element.text_content()}  month {td_element.get_attribute("data-month")}  year  {td_element.get_attribute("data-year")}'
                    )
                except Exception:
                    print(f"Inside Exception ")
                    continue

                cal_date = datetime(year, month, day)
                print(cal_date)
                if cal_date >= cur_date:
                    print("inside break condition")
                    return False, False
                found_date = cal_date
                return True, False

        return False, True

    def get_date(self):
        global cur_date
        date_text = self.page.locator(appointment_date_id).text_content()
        date_text = date_text.replace("\n", "")

        matches = re.search(appointment_date_regex, date_text)

        if matches:
            print(
                "Match was found at {start}-{end}: {match}".format(
                    start=matches.start(), end=matches.end(), match=matches.group()
                )
            )

            assert len(matches.groups()) == 1

            date_text = matches.group(1)
            date_text = date_text.strip()
            date_obj = parser.parse(date_text)
            print(f"current date is {date_obj}")
            cur_date = date_obj
            return date_obj

    def select_location(self, option):
        if option in locations:
            self.page.locator(location_id).select_option(option)
            self.page.wait_for_load_state("networkidle")
            time.sleep(0.5)

    def is_date_available(self, wait_time: int = 500):
        try:
            self.page.wait_for_selector(not_available_id, timeout=wait_time)
            return False
        except TimeoutError:
            return True

    def run_check(self):
        global cur_date
        global found_date

        for loc in visa_locations:
            print(f"checking for {loc} location")
            self.select_location(loc)

            if self.is_date_available():
                if not cur_date:
                    current_date = datetime.now()
                    # Calculate date two months in the future
                    cur_date = current_date + timedelta(days=3 * 30)

                con = True
                print(f"Start Searching, current date is :{cur_date}")
                self.page.locator(calender_dropdown_date_id).click()
                # replace with while True
                while con:
                    print(f"contine {con}")
                    result, con = self.check_availability(cur_date)

                    if result:
                        print("got the date,, book {}")
                        date_string = found_date.strftime("%Y-%m-%d %H:%M:%S")
                        print(date_string)
                        exit(0)

                    else:
                        for _ in range(2):
                            self.page.get_by_text("Next").click()
                            month = self.page.locator(
                                calender_month_id
                            ).first.text_content()

                            m = month_to_num(month[:3].lower())

                            y = int(
                                self.page.locator(calender_year_id).first.text_content()
                            )
                            new_date = datetime(y, m, 1)
                            if new_date > cur_date:
                                con = False

                self.page.keyboard.press("Escape")

            else:
                print(f"No dates available for {loc}")

    def close_browser(self):
        self.browser.close()


def main():
    v = VisaAutomate()
    v.login(username=user, passwd=password, cont=False)
    v.get_date()
    v.go_to_appointments(appointment_id)
    v.run_check()
    # v.close_browser()


if __name__ == "__main__":
    v = VisaAutomate()
    v.login(username=user, passwd=password, cont=False)
    v.get_date()
    v.go_to_appointments(appointment_id)
    v.run_check()
