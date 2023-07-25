
from tests.test_base_authorization import test_auth_paswrd
from tests.test_base_ragistation import test_reg_data
import pytest
from locators import LOCATOR_ID_NUM_LC, LOCATOR_ID_LOGIN, LOCATOR_ID_MAIL, LOCATOR_ID_PHONE
from settings import valid_auth_number, worded_auth_number, wronge_auth_number
from settings import valid_login, empty_login, wronge_login, empty_mail, wronge_mail
from settings import valid_passwrd, valid_phone, name, last_name, valid_mail
from settings import empty_name, wronge_name, wronge_last_name, empty_passwrd
from settings import empty_last_name, empty_phone, wronge_phone, wronge_passwrd


@pytest.mark.parametrize("passwrd,auth_number,exp,locator", [

(valid_passwrd,valid_auth_number,1,LOCATOR_ID_NUM_LC),
(valid_passwrd,valid_mail,1,LOCATOR_ID_MAIL),
(valid_passwrd,valid_login,1,LOCATOR_ID_LOGIN),
(valid_passwrd,valid_phone,1,LOCATOR_ID_PHONE),
(valid_passwrd,wronge_auth_number,0,LOCATOR_ID_NUM_LC),
(valid_passwrd,worded_auth_number,0,LOCATOR_ID_NUM_LC),
(wronge_passwrd,valid_auth_number,0,LOCATOR_ID_NUM_LC),
(valid_passwrd,empty_login,0,LOCATOR_ID_LOGIN),
(valid_passwrd,wronge_login,0,LOCATOR_ID_LOGIN),
(valid_passwrd,empty_mail,0,LOCATOR_ID_MAIL),
(valid_passwrd,wronge_mail,0,LOCATOR_ID_MAIL),
(valid_passwrd,empty_phone,0,LOCATOR_ID_PHONE),
(valid_passwrd,wronge_phone,0,LOCATOR_ID_PHONE)])


def test1_act_auth_paswrd(passwrd, auth_number, exp,locator):
    assert test_auth_paswrd(passwrd, auth_number, locator) == exp


@pytest.mark.parametrize("name,last_name,phone,passwrd,exp", [
    (name, last_name, valid_phone, valid_passwrd, 2),
    (wronge_name, last_name, valid_phone, valid_passwrd, 2),
    (empty_name, last_name, valid_phone, valid_passwrd, 0),
    (name, wronge_last_name, valid_phone, valid_passwrd, 2),
    (name, empty_last_name, valid_phone, valid_passwrd, 0),
    (name, last_name, empty_phone, valid_passwrd, 0),
    (name, last_name, wronge_phone, valid_passwrd, 0),
    (name, last_name, valid_phone, wronge_passwrd, 2),
    (name, last_name, valid_phone, empty_passwrd, 0)])


def test2_act_registration(name, last_name, phone, passwrd, exp):
    assert test_reg_data(name, last_name, phone, passwrd) == exp
