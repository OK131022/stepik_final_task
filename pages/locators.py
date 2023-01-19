import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By

class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/"
    LOGIN_LINK = (By.ID, "login_link")
    
class LoginPageLocators():
    LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    SUBSTRING_LOGIN = "login"
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_ADDR_INPUT = (By.ID, "id_registration-email")
    PASSWORD1_INPUT = (By.ID, "id_registration-password1")
    PASSWORD2_INPUT = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")