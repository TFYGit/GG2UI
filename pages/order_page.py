# 编码人：TFY
# 时间：2022/6/4
from common.browser_actions import Browser


class OrderPage(Browser):

    # 顶部筛选项
    # 全部
    all_button = ('xpath', "(//button[@type='button'])[2]")

    # 进行中
    conduct_button = ('xpath', "(//button[@type='button'])[3]")

    # 已完成
    finish_button = ('xpath', "(//button[@type='button'])[4]")

    # 争议
    dispute_button = ('xpath', "(//button[@type='button'])[5]")

    # 已退款
    refunded_button = ('xpath', "(//button[@type='button'])[6]")

    # 已关闭
    closed_button = ('xpath', "(//button[@type='button'])[7]")

    # 筛选按钮
    filter_button = ('xpath', "//div[@class='filters filters-active']")

    # 类型选择下拉框
    type_selection = ('xpath', "//div[@class='selector']")

    # 购买开始时间输入框
    starting_time_input = ('xpath', "//input[@placeholder='开始时间']")

    # 购买结束时间输入框
    end_time_input = ('xpath', "//input[@placeholder='结束时间']")