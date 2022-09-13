from selene import be, have
from selene.support.shared import browser
import pytest
from data_for_test import filling_date, check_form_data
import os


def test_submit_date():
    filling_date()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    check_form_data()




