#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from unittestzero import Assert

from pages.signup import SignUpPage
from pages.signin import SignInPage
from pages.home import HomePage
from mocks.mock_user import MockUser


class TestManageAccount:

    def test_can_create_new_user_account(self, mozwebqa):
    	"""https://moztrap.allizom.org/manage/case/272/"""

        user = MockUser()
        signup = SignUpPage(mozwebqa)
        signup.go_to_page()
        signup.sign_up(user)

        # do email verification
        signup.do_verify_email(user)

        # verify now logged in
        home_pg = HomePage(mozwebqa)
        home_pg.go_to_page()
        Assert.true(home_pg.is_logged_in)
        Assert.true(home_pg.is_manage_section_visible)

    @pytest.mark.nondestructive
    def test_that_user_can_sign_in_and_out(self, mozwebqa):
    	"""https://moztrap.allizom.org/manage/case/273/"""

        sign_in = SignInPage(mozwebqa)
        sign_in.go_to_page()
        user = mozwebqa.credentials['default']
        home_pg = sign_in.sign_in(user)
        Assert.true(home_pg.is_logged_in)

        # sign out
        home_pg.sign_out()
        Assert.false(home_pg.is_logged_in)

    @pytest.mark.destructive
    def test_that_user_can_change_password(self, mozwebqa):
    	"""https://moztrap.allizom.org/manage/case/274/"""
    	pytest.skip("not implemented yet")

    @pytest.mark.destructive
    def test_that_user_can_cancel_account(self, mozwebqa):
    	"""https://moztrap.allizom.org/manage/case/275/"""
    	pytest.skip()

