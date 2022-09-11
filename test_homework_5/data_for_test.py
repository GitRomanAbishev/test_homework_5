import pytest
from selene.support.shared import browser


def filling_date():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Name')
    browser.element('#lastName').type('Last Name')
    browser.element('#userEmail').type('some@Email.ru')
    browser.element('#userNumber').type('7963123458')
    browser.element('//*[@id="subjectsInput"]').type('Some Subjects')
    browser.element('//*[@id="currentAddress"]').type('Some address')
    browser.element('[for="gender-radio-1"').click()
    browser.element('[for="hobbies-checkbox-1"').click()
    browser.element('[for="hobbies-checkbox-2"').click()
    browser.element('[for="hobbies-checkbox-3"').click()
    browser.element('#dateOfBirthInput').click().element('//*[@class="react-datepicker__week"] [4]').click()
    browser.element('#uploadPicture').send_keys(
        "C:/Users/r.abishev/PycharmProjects/test_homework_5/demoqa_test/files_for_tests/for_test.txt")
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()
    # Скажите у нас будет обяъснения как получить селекторы для элементов которые исчезают?
    #В этом задании для элементов из выпадающего списка мне помог коллега фронтендер дергуть id элементов
    #У меня не получалось