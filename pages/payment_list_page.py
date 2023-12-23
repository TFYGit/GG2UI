# 编码人：TFY
# 时间：2023/12/23
from common.browser_actions import Browser


class PaymentListPage(Browser):
    """
    唤醒支付列表查看支付方式是否正常拉起
    """
    # 支付列表内的支付方式
    payment_method1 = ('xpath', "(//label[@for='input-0'])[1]")
    payment_method2 = ('xpath', "(//label[@for='input-1'])[1]")
    payment_method3 = ('xpath', "(//label[@for='input-2'])[1]")
    payment_method4 = ('xpath', "(//label[@for='input-3'])[1]")

    # URL
    frontPage_url = "https://www.gamsgo.com/"

    # session弹窗关闭按钮
    close_session = ('xpath', "//div[@class='iconfont icon-close close']")

    # 首页立即购买按钮
    buy_button = ('xpath', "(//button[@type='button'])[3]")

    # 支付弹窗前往付款按钮
    payment_button = ('xpath', "(//span[text()='前往付款'])[2]")

    # 访问首页
    def goto(self):
        self.visit(self.frontPage_url)

    # 关闭session弹窗
    def close_session_method(self):
        self.mouse_click(self.close_session)

    # 首页点击立即购买按钮拉起购买弹窗
    def purchase_pop_up(self):
        self.mouse_click(self.buy_button)

    # 支付弹窗点击前往付款按钮
    def click_payment_button(self):
        self.mouse_click(self.payment_button)

    # 美国节点支付列表选中第一个支付方式
    def us_payment_list_m1(self):
        self.mouse_click(self.payment_method1)

    # 美国节点支付列表选中第二个支付方式
    def us_payment_list_m2(self):
        self.mouse_click(self.payment_method2)

    # 美国节点支付列表选中第三个支付方式
    def us_payment_list_m3(self):
        self.mouse_click(self.payment_method3)

    # 美国节点支付列表选中第四个支付方式
    def us_payment_list_m4(self):
        self.mouse_click(self.payment_method4)
