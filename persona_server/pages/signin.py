#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page import Page
from pages.home import HomePage


class SignInPage(Page):

    _page_title = 'Mozilla Persona: Sign In'
    _page_url = '/signin'

    _email_field_locator = (By.ID, 'email')
    _sign_in_locator = (By.CSS_SELECTOR, 'div.cf button')
    _password_field_locator = (By.ID, 'password')

    def fill_email_field(self, email):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.is_element_visible(*self._email_field_locator),
            "email field did not appear within %s" % self.timeout)
        self.selenium.find_element(*self._email_field_locator).send_keys(email)

    def request_sign_in(self):
        self.selenium.find_element(*self._sign_in_locator).click()

    def fill_password_field(self, password):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.is_element_visible(*self._password_field_locator),
            "Password field did not appear within %s" % self.timeout
        )
        self.selenium.find_element(*self._password_field_locator).send_keys(password)

    def sign_in(self, user):
        """Takes a user (Mock or credentials) and signs in."""
        # fill email and verify
        self.fill_email_field(self._get_email_from_user(user))
        self.request_sign_in()
        # fill password field and submit again
        self.fill_password_field(user['password'])
        self.request_sign_in()
        home_pg = HomePage(self.testsetup)
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: home_pg.is_manage_section_visible,
            "manage section / home page did not appear")
        return home_pg
