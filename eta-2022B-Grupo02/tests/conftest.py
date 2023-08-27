import time

import pytest

from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
#from pages.ProductsPage import ProductsPage


def pytest_addoption(parser):
    parser.addoption("--select_browser", default="chrome", help="Select browser")


@pytest.fixture
def select_browser(request):
    yield request.config.getoption("--select_browser").lower()


@pytest.fixture()
def setup(select_browser):
    home_page = HomePage(browser=select_browser)
    yield home_page
    #home_page.close()


@pytest.fixture
def run_all_browser(all_browser):
    home_page = HomePage(browser=all_browser)
    yield home_page
    #home_page.close()