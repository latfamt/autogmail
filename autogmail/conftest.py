import pytest
from selenium import webdriver
import os


@pytest.fixture(scope="function")
def driver_init(request):
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'chromedriver.exe')
    web_driver = webdriver.Chrome(filename)
    web_driver.get('http://google.ru')
    web_driver.maximize_window()
    web_driver.implicitly_wait(30)
    request.cls.driver = web_driver
    yield
    web_driver.quit()


def pytest_addoption(parser):
    parser.addoption("--sender_email", action="store")
    parser.addoption("--sender_password", action="store")

    parser.addoption("--receiver_email", action="store")
    parser.addoption("--receiver_password", action="store")


def pytest_generate_tests(metafunc):
    option_sender_email = metafunc.config.option.sender_email
    option_sender_password = metafunc.config.option.sender_password
    option_receiver_email = metafunc.config.option.receiver_email
    option_receiver_password = metafunc.config.option.receiver_password

    if "sender_email" in metafunc.fixturenames and option_sender_email is not None:
        metafunc.parametrize("sender_email", [option_sender_email])
    if "sender_password" in metafunc.fixturenames and option_sender_password is not None:
        metafunc.parametrize("sender_password", [option_sender_password])
    if "receiver_email" in metafunc.fixturenames and option_receiver_email is not None:
        metafunc.parametrize("receiver_email", [option_receiver_email])
    if "receiver_password" in metafunc.fixturenames and option_receiver_password is not None:
        metafunc.parametrize("receiver_password", [option_receiver_password])