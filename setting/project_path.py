# 编码人：TFY
# 时间：2022/6/24
import os

# 项目根路径
root_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 输出报告路径
output_report_path = os.path.join(root_directory, 'cases/output')

# 历史报告路径
historical_report_path = os.path.join(root_directory, 'cases/historical_report')

# 日志保存路径
log_info = os.path.join(root_directory, 'logs/info/info.txt')
log_debug = os.path.join(root_directory, 'logs/debug/debug.txt')
log_error = os.path.join(root_directory, 'logs/error/error.txt')


