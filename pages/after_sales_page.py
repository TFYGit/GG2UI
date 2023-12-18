# 编码人：TFY
# 时间：2022/6/4
# 售后支持页
from common.browser_actions import Browser


class AfterSalesPage(Browser):

    # 在线聊天按钮
    chat_button = ('xpath', "(//div[@class='block cursor-pointer'])[1]")

    # 帮助中心按钮
    help_center_button = ('xpath', "(//div[@class='block cursor-pointer'])[2]")

    # 创建新工单按钮
    work_order_button = ('xpath', "(//button[@type='button'])[2]")

    # 搜索输入框
    search_input = ('xpath', "//input[@placeholder='搜索订阅帐户...']")




