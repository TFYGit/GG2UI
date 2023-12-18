# 编码人：TFY
# 时间：2022/6/24
import os
import shutil

from setting.project_path import output_report_path, historical_report_path


class HandleMoveReport:

    def __init__(self):
        pass

    # 移动报告的历史记录到指定文件夹下
    def move_report(self):
        # 获取文件路径下所有的文件名
        file_names = os.listdir(output_report_path)
        # 将文件挪动到指定文件夹下
        for file_name in file_names:
            f = os.path.join(output_report_path, file_name)
            shutil.move(f, historical_report_path)


if __name__ == '__main__':
    cl = HandleMoveReport()
    print(cl.move_report())