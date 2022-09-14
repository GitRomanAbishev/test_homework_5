import os
import pytest
from selene.support.shared import browser
from selene import have, be


def filling_date():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Name')
    browser.element('#lastName').type('Last Name')
    browser.element('#userEmail').type('some@Email.ru')
    browser.element('#userNumber').type('7963123458')
    browser.element('//*[@id="subjectsInput"]').type('Maths').press_enter()
    browser.element('//*[@id="currentAddress"]').type('Some address')
    browser.element('[for="gender-radio-1"').click()
    browser.element('[for="hobbies-checkbox-1"').click()
    browser.element('[for="hobbies-checkbox-2"').click()
    browser.element('[for="hobbies-checkbox-3"').click()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').type('2021')
    browser.element('.react-datepicker__month-select').type('April')
    browser.element('[aria-label="Choose Thursday, April 15th, 2021"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('files_for_tests/test_picture.png'))
    browser.element('#state').click()
    browser.element('#react-select-3-option-0').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-0').click()


# Эту часть честно признаюсь подсмотрел, так как не разобрался, но когда посомтрел разобрался!
def check_form_data():
    #Так явно лучше
    browser.all('.modal-body td:nth-child(even)').should(have.texts(
        'Name Last Name',
        'some@Email.ru',
        'Male',
        '7963123458',
        '15 April,2021',
        'Maths',
        'Sports, Reading, Music',
        'test_picture.png',
        'Some address',
        'NCR Delhi'
    ))
    # browser.element('#example-modal-sizes-title-lg').should(be.visible).should(
    #     have.text('Thanks for submitting the form'))
    # browser.element('.table-responsive').should(have.text('Name' + ' ' + 'Last Name'))
    # browser.element('.table-responsive').should(have.text('some@Email.ru'))
    # browser.element('.table-responsive').should(have.text('Male'))
    # browser.element('.table-responsive').should(have.text('7963123458'))
    # browser.element('.table-responsive').should(have.text('15 April,2021'))
    # browser.element('.table-responsive').should(have.text('Maths'))
    # browser.element('.table-responsive').should(have.text('Sports, Reading, Music'))
    # browser.element('.table-responsive').should(have.text('test_picture.png'))
    # browser.element('.table-responsive').should(have.text('Some address'))
    # browser.element('.table-responsive').should(have.text('NCR Delhi'))