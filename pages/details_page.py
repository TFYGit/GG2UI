# 编码人：TFY
# 时间：2023/12/17
from common.browser_actions import Browser


class DetailsPage(Browser):

    # blog按钮
    blog_button = ('xpath', "")

    # 购买按钮
    detail_buy_button = ('xpath', "")

    # 底部推荐栏按钮
    recommend_button = ('xpath', "")