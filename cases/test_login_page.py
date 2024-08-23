# 编码人：TFY
# 时间：2022/6/4
import pytest
import time

from pages.login_page import LoginPage


@pytest.mark.login
class TestLoginPage:

    def test_login_page_method1(self, fixture):
        """
        1、点击谷歌快捷登录按钮
        2、输入邮箱
        3、输入密码
        4、登录
        :param fixture:
        :return:
        """
        lp = LoginPage(fixture)
        # 访问登陆站
        lp.goto()
        time.sleep(3)
        # 等待元素加载完成
        # lp.load_complete()
        # 点击谷歌快捷登录按钮
        lp.click_google_button()
        time.sleep(2)
        # 输入谷歌邮箱
        lp.input_google_email()
        time.sleep(2)
        # 点击下一步
        lp.click_next_button()
        time.sleep(5)
        # 输入谷歌密码
        lp.input_google_password()
        time.sleep(3)
        # 点击下一步
        lp.click_next_button()
        time.sleep(8)
