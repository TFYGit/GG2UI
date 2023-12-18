# 编码人：TFY
# 时间：2022/6/4
from common.browser_actions import Browser


class PersonalCenterPage(Browser):

    # 昵称编辑按钮
    editnickname_button = ('xpath', "(//span[text()='编辑'])[1]")

    # 邮箱编辑按钮
    editemail_button = ('xpath', "(//span[text()='编辑'])[2]")