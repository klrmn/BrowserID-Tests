#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from page import Page


class HomePage(Page):

    _page_title = 'Mozilla Persona: A Better Way to Sign In'
    _page_url = '/'
    _sign_in_locator = (By.CSS_SELECTOR, 'a.signIn')
    _sign_up_locator = (By.CSS_SELECTOR, 'a.button.create')
    _manage_section_locator = (By.ID, 'manage')
    _sign_out_locator = (By.CSS_SELECTOR, 'a.signOut')

    def click_sign_up(self):
        self.selenium.find_element(*self._sign_up_locator).click()
        from pages.signup import SignUpPage
        return SignUpPage(self.testsetup)

    @property
    def is_manage_section_visible(self):
        return self.is_element_visible(*self._manage_section_locator)

    @property
    def is_logged_in(self):
        return self.is_element_visible(*self._sign_out_locator)

    def sign_out(self):
        self.selenium.find_element(*self._sign_out_locator).click()
