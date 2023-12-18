# 编码人：TFY
# 时间：2023/12/17
from common.browser_actions import Browser


class LoginPage(Browser):

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
    lgin_button = ('xpath', "//button[@type='button']")

    # 左上角logo
    logo_button = ('xpath', "//div[@class='v-responsive__content']")
