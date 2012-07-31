#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from page import Page


class VerifyEmailPage(Page):

    _page_title = 'Mozilla Persona: Complete Registration'

    _message_locator = (By.CSS_SELECTOR, 'div#congrats')
    _error_locator = (By.ID, 'error_contents')

    def __init__(self, testsetup, url):
        """Takes testsetup (or mozwebqa) and the url that is output from RestMail.Email.verify_user_link()."""
        Page.__init__(self, testsetup)
        self.selenium.get(url)
        self.is_the_current_page
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.is_element_visible(*self._message_locator) or \
                      self.is_element_visible(*self._error_locator),
            "verify email page does not appear to have loaded fully"
        )
