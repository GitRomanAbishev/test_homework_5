from selene import be, have
from selene.support.shared import browser
import pytest
from data_for_test import filling_date

def test_submit_date():
    filling_date()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').vizibale = True
    # А это работает вообще? я проверяю видимость элемента?
    # Все данные для заполнения описаны в функции filling_date и импортированны
    # Скажите, нормально, что я все данные ввожу в функции за приделами теста?

