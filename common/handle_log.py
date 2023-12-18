# 编码人：TFY
# 时间：2022/6/25
import logging
from logging import handlers

from setting.project_path import log_info, log_debug, log_error


def get_log():
    # 创建日志收集器
    collector = logging.getLogger('test_01')
    # 收集器设置日志收集级别
    collector.setLevel(logging.DEBUG)
    # 创建收集渠道
    channel_info = handlers.TimedRotatingFileHandler(when='D', encoding='utf-8', interval=1, filename=log_info)
    channel_debug = handlers.TimedRotatingFileHandler(when='D', encoding='utf-8', interval=1, filename=log_debug)
    channel_error = handlers.TimedRotatingFileHandler(when='D', encoding='utf-8', interval=1, filename=log_error)
    # 渠道日志收集级别
    channel_info_filter = logging.Filter()
    channel_info_filter.filter = lambda a: logging.DEBUG < a.levelno <= logging.INFO
    channel_debug_filter = logging.Filter()
    channel_debug_filter.filter = lambda a: logging.DEBUG <= a.levelno < logging.INFO
    channel_error_filter = logging.Filter()
    channel_error_filter.filter = lambda a: logging.WARNING < a.levelno <= logging.ERROR
    # 渠道绑定收集级别
    channel_info.addFilter(channel_info_filter)
    channel_debug.addFilter(channel_debug_filter)
    channel_error.addFilter(channel_error_filter)
    # 创建日志格式
    mat = '【%(thread)d->%(asctime)s-%(filename)s-%(levelname)s】 >>> %(message)s'
    log_mat = logging.Formatter(mat)
    # 格式绑定渠道
    channel_info.setFormatter(log_mat)
    channel_debug.setFormatter(log_mat)
    channel_error.setFormatter(log_mat)
    # 渠道绑定收集器
    collector.addHandler(channel_info)
    collector.addHandler(channel_debug)
    collector.addHandler(channel_error)
    # 返回配置好的收集器
    return collector


log = get_log()
