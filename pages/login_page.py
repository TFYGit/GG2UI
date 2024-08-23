# 编码人：TFY
# 时间：2023/12/17
from common.browser_actions import Browser


class LoginPage(Browser):

    # 登录站URL
    login_url = ("https://account.gamsgo.com/Login")

    # 邮箱输入框
    mail_input = ('xpath', "//input[@placeholder='邮箱']")

    # 下一步按钮
    continue_button = ('xpath', "(//button[@type='button'])[4]")

    # 密码输入框
    password_input = ('xpath', "//input[@placeholder='密码']")

    # 忘记密码按钮
    forget_password_button = ('xpath', "//a[@class='text-left mr-2']")

    # 使用验证码登录按钮
    code_login_button = ('xpath', "//a[@class='text-right']")

    # 免费加入按钮
    free_to_join_button = ('xpath', "//a[@class='register-link']")

    # 条款按钮
    terms_button = ('xpath', "(//a[@href='https://gg2.gamsgo.cc/terms-conditions'])[1]")

    # 隐私政策
    privacy_policy_button = ('xpath', "(//a[@href='https://gg2.gamsgo.cc/privacy-policy'])[1]")

    # 底部条款按钮
    terms_button02 = ('xpath', "(//a[@href='https://gg2.gamsgo.cc/terms-conditions'])[2]")

    # 底部隐私政策按钮
    privacy_policy_button02 = ('xpath', "(//a[@href='https://gg2.gamsgo.cc/privacy-policy'])[2]")

    # 登录按钮
    login_button = ('xpath', "//button[@type='button']")

    # 左上角logo
    logo_button = ('xpath', "//div[@class='v-responsive__content']")

    # 谷歌快捷登录按钮
    google_button = ('xpath', "(//button[@type='button'])[1]")

    # facebook快捷登录按钮
    facebook_button = ('xpath', "(//button[@type='button'])[2]")

    # kakao快捷登录按钮
    kakao_button = ('xpath', "(//button[@type='button'])[3]")

    # 谷歌账号输入框
    google_email_input = ('xpath', "//input[@type='email']")

    # 谷歌邮箱输入弹窗下一步按钮
    next_button = ('xpath', "//span[text()='下一步']")

    # 谷歌账号密码输入框
    google_password_input = ('xpath', "//input[@type='password']")

    # 元素加载完成
    def load_complete(self):
        self.wait_presence(self.google_button)
        self.wait_presence(self.facebook_button)
        self.wait_presence(self.google_email_input)
        self.wait_presence(self.next_button)
        self.wait_presence(self.google_password_input)
        self.wait_presence(self.kakao_button)

    # 访问登录站
    def goto(self):
        self.visit(self.login_url)

    # 输入账号
    def mail_input_method(self):
        self.input_content(self.mail_input, "ceshi221@gamsgo.xyz")

    # 点击下一步按钮
    def click_continue_button_method(self):
        self.mouse_click(self.continue_button)

    # 输入密码
    def password_input_method(self):
        self.input_content(self.password_input, "tfy12345")

    # 点击登录按钮
    def click_lgin_button(self):
        self.mouse_click(self.login_button)

    # 点击谷歌快捷登录按钮
    def click_google_button(self):
        self.mouse_click(self.google_button)

    # 点击facebook快捷登录按钮
    def click_facebook_button(self):
        self.mouse_click(self.facebook_button)

    # 点击kakao快捷登录按钮
    def click_kakao_button(self):
        self.mouse_click(self.kakao_button)

    # 输入谷歌邮箱
    def input_google_email(self):
        self.input_content(self.google_email_input, "tfy125800@gmail.com")

    # 输入谷歌邮箱密码
    def input_google_password(self):
        self.input_content(self.google_password_input, "tfy125800...")

    # 点击下一步按钮
    def click_next_button(self):
        self.mouse_click(self.next_button)



