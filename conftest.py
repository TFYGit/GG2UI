# 编码人：TFY
# 时间：2022/5/29
import pytest
from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions

from pages.front_page import FrontPage


@pytest.fixture()
def fixture():
    # 先设置浏览器的属性
    option = ChromiumOptions()
    option.page_load_strategy = 'eager'
    # 1、得到一个浏览器对象。
    driver = webdriver.Chrome(options=option)
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


# 登录
# @pytest.fixture()
# def login_fixture(fixture):
#     root_page = FrontPage(fixture)
#     root_page.goto()
#     root_page.login(user_name='13050570625', password='tfy125800')


# @pytest.fixture()
# def root_page(fixture):
#     return RootPage(fixture)
#
#
# @pytest.fixture()
# def login_page(fixture):
#     return LoginPage(fixture)
#
#
# @pytest.fixture()
# def register_page(fixture):
#     return RegisterPage(fixture)
#
#
# @pytest.fixture()
# def product_list_page(fixture):
#     return ProductListPage(fixture)
#
#
# @pytest.fixture()
# def product_details_page(fixture):
#     return ProductDetailsPage(fixture)
#
#
# @pytest.fixture()
# def order_submission_page(fixture):
#     return OrderSubmissionPage(fixture)