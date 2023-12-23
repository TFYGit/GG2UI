# 编码人：TFY
# 时间：2022/6/4

import pytest
import time

from pages.front_page import FrontPage


@pytest.mark.login
class TestFrontPage:

    def test_front_page_method1(self, fixture):
        """
        1、访问主页面
        2、关闭session弹窗
        3、首页点击立即购买按钮拉起购买弹窗
        4、点击支付弹窗关闭按钮
        5、点击“+”拉起支付弹窗
        6、点击支付弹窗关闭按钮
        7、点击联盟计划按钮
        8、点击查看详情按钮跳转详情页
        :param fixture:
        :return:
        """
        front_page = FrontPage(fixture)
        # 访问主页面
        front_page.goto()
        # 关闭session弹窗
        front_page.close_session_method()
        time.sleep(3)
        # 首页点击立即购买按钮拉起购买弹窗
        front_page.purchase_pop_up()
        time.sleep(3)
        # 点击支付弹窗关闭按钮
        front_page.close_pop()
        time.sleep(3)
        # 点击“+”拉起支付弹窗
        front_page.click_plus()
        time.sleep(3)
        # 点击支付弹窗关闭按钮
        front_page.close_pop()
        time.sleep(3)
        # 点击查看详情按钮跳转详情页
        front_page.details_page()
        time.sleep(8)

