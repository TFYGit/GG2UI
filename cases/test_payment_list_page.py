# 编码人：TFY
# 时间：2023/12/23

import pytest
import time
from pages.payment_list_page import PaymentListPage
from pages.login_page import LoginPage
from pages.front_page import FrontPage


@pytest.mark.payment
class TestPatmentListPage:

    def test_patment_list_page_method1(self, fixture):
        """
        1、登录网站访问首页
        2、关闭session弹窗
        3、点击立即购买按钮
        4、选择支付方式拉起第三方支付弹窗
        :param fixture:
        :return:
        """
        ptp = PaymentListPage(fixture)
        lp = LoginPage(fixture)
        fp = FrontPage(fixture)
        # 访问首页
        # fp.goto()
        # # 点击右上角头像
        # fp.click_avatar_button()
        # time.sleep(1)
        # # 点击登录按钮
        # fp.click_login_button()
        # time.sleep(3)

        # 访问登录站
        lp.goto()
        # 输入邮箱
        lp.mail_input_method()
        # 点击下一步按钮
        lp.click_continue_button_method()
        # 输入密码
        lp.password_input_method()
        time.sleep(2)
        # 点击登录
        lp.click_lgin_button()
        time.sleep(5)
        # 关闭session弹窗
        # ptp.close_session_method()
        # time.sleep(3)
        # 点击立即购买按钮
        ptp.purchase_pop_up()
        time.sleep(2)
        # 点击前往付款按钮
        fp.click_payment_button()
        time.sleep(2)
        # 选中支付方法
        # ptp.us_payment_list_m1()
        ptp.us_payment_list_m2()
        # ptp.us_payment_list_m3()
        # ptp.us_payment_list_m4()
        # 点击前往付款按钮
        ptp.click_payment_button()
        time.sleep(8)
