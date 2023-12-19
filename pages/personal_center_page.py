# 编码人：TFY
# 时间：2022/6/4
from common.browser_actions import Browser


class PersonalCenterPage(Browser):

    # 昵称编辑按钮
    edit_nickname_button = ('xpath', "(//span[text()='编辑'])[1]")

    # 邮箱编辑按钮
    edit_email_button = ('xpath', "(//span[text()='编辑'])[2]")