from common.browser_actions import Browser


class FrontPage(Browser):

    # URL
    frontPage_url = "https://www.gamsgo.com/"

    # 右上角头像
    avatar_button = ('xpath', "(//button[@type='button'])[1]")

    # 头像菜单内订阅按钮
    avatar_subscription_button = ('xpath', "(//a[@href='/subscription'])[2]")

    # 头像菜单内售后按钮
    avatar_after_sales_button = ('xpath', "(//a[@href='/support/ticketlist'])[3]")

    # 头像菜单内帮助中心按钮
    avatar_help_center_button = ('xpath', "//a[@href='https://help.gamsgo.com/']")

    # 头像菜单内订单按钮
    avatar_order_button = ('xpath', "//a[@href='/order']")

    # 头像菜单内联盟计划按钮
    avatar_aff_button = ('xpath', "(//a[@href='/affiliate/program'])[3]")

    # 首页登录按钮
    login_button = ('xpath', "//span[text() = '登录 / 加入']")

    # session弹窗关闭按钮
    close_session = ('xpath', "(//button[@type='button'])[12]")

    # 订阅卡片“+”按钮
    plus_button = ('xpath', "(//img[@preset='webp'])[1]")

    # 立即购买按钮
    buy_button = ('xpath', "(//button[@type='button'])[3]")

    # 查看更多详情
    details_button = ('xpath', "(//a[text()='查看更多详情'])[1]")

    # 支付弹窗关闭按钮
    closure_button = ('xpath', "(//div[@class='iconfont icon-close'])[1]")

    # 联盟计划按钮
    aff_button = ('xpath', "//span[text()='联盟计划']")

    # 售后支持按钮
    after_sales_button = ('xpath', "//span[text()='售后支持']")

    # 订阅按钮
    subscription_button = ('xpath', "//span[text()='订阅']")

    # 购买弹窗内的前往付款按钮
    payment_button = ('xpath', "(//span[text()='前往付款'])[1]")

    # 访问首页
    def goto(self):
        self.visit(self.frontPage_url)

    # 点击右上角头像
    def click_avatar_button(self):
        self.mouse_click(self.avatar_button)

    # 点击登录按钮
    def click_login_button(self):
        self.mouse_click(self.login_button)

    # 关闭session弹窗
    def close_session_method(self):
        self.mouse_click(self.close_session)

    # 首页点击立即购买按钮拉起购买弹窗
    def purchase_pop_up(self):
        self.mouse_click(self.buy_button)

    # 点击“+”拉起支付弹窗
    def click_plus(self):
        self.mouse_click(self.plus_button)

    # 点击支付弹窗关闭按钮
    def close_pop(self):
        self.mouse_click(self.closure_button)

    # 点击查看详情按钮跳转详情页
    def details_page(self):
        self.mouse_click(self.details_button)

    # 点击登录按钮跳转登录站
    def click_login(self):
        self.mouse_click(self.login_button)

    # 点击联盟计划按钮
    def click_aff_button(self):
        self.mouse_click(self.aff_button)

    # 点击售后支持按钮
    def click_after_sales_button(self):
        self.mouse_click(self.after_sales_button)

    # 点击订阅按钮
    def click_subscription_button(self):
        self.mouse_click(self.subscription_button)

    # 点击前往付款按钮
    def click_payment_button(self):
        self.mouse_click(self.payment_button)

