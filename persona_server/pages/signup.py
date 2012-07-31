#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page import Page
from restmail.restmail import RestmailInbox


class SignUpPage(Page):

    _page_title = 'Mozilla Persona: Sign Up'
    _page_url = '/signup'

    _email_field_locator = (By.ID, 'email')
    _verify_email_locator = (By.CSS_SELECTOR, 'div.cf button')
    _password_field_locator = (By.ID, 'password')
    _password_verify_field_locator = (By.ID, 'vpassword')

    def fill_email_field(self, email):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.is_element_visible(*self._email_field_locator),
            "email field did not appear within %s" % self.timeout)
        self.selenium.find_element(*self._email_field_locator).send_keys(email)

    def request_verify_email(self):
        self.selenium.find_element(*self._verify_email_locator).click()

    def wait_for_password_fields(self):
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: \
                self.is_element_visible(*self._password_field_locator) and \
                self.is_element_visible(*self._password_verify_field_locator), \
            "Password fields did not appear within %s" % self.timeout 
        )

    def fill_password_field(self, password):
        self.selenium.find_element(*self._password_field_locator).send_keys(password)

    def fill_password_verify_field(self, password):
        self.selenium.find_element(*self._password_verify_field_locator).send_keys(password)

    def sign_up(self, user):
        """Takes a user (Mock or credentials) and does all the steps to prompt verification email."""
        # fill email and verify
        self.fill_email_field(user['email'])
        self.request_verify_email()
        # password fields should become visible
        self.wait_for_password_fields() # will throw error on Timeout
        # fill password fields and verify again
        self.fill_password_field(user['password'])
        self.fill_password_verify_field(user['password'])
        self.request_verify_email()

    def do_verify_email(self, user):
        """Takes (Mock) User, checks their email, finds the link and loads it."""

        inbox = RestmailInbox(user['email'])
        email = inbox.find_by_index(0)

        # Load the BrowserID link from the email in the browser
        from pages.verify_email import VerifyEmailPage
        verify = VerifyEmailPage(self.testsetup, email.verify_user_link)
        return verify
