#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from unittestzero import Assert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException


class Page(object):

    def __init__(self, testsetup):
        self.testsetup = testsetup
        self.base_url = testsetup.base_url
        self.selenium = testsetup.selenium
        self.timeout = testsetup.timeout

    @property
    def is_the_current_page(self):
        if self._page_title:
            WebDriverWait(self.selenium, self.timeout).until(lambda s: s.title)

        Assert.equal(self.selenium.title, self._page_title)
        return True

    def go_to_page(self):
        if self._page_url:
            self.selenium.get(self.base_url + self._page_url)
            self.is_the_current_page
        ### do something if _page_url doesn't exist?

    def is_element_present(self, *locator):
        self.selenium.implicitly_wait(0)
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.testsetup.default_implicit_wait)

    def is_element_visible(self, *locator):
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except NoSuchElementException, ElementNotVisibleException:
            return False

    def _get_email_from_user(self, user):
        """Handles the differing formats of BIDPOM MockUsers vs credentials users."""
        email = ""
        try:
            email = user['primary_email']
        except KeyError:
            email = user['email']
        return email