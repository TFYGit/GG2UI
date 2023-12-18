# 编码人：TFY
# 时间：2022/6/4
import allure
from faker import Faker
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from common.handle_mysql import HandleMySql
from common.handle_log import log


class Browser:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    # 页面截图
    def page_screenshot(self, name):
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)

    # 访问页面
    def visit(self, url):
        try:
            self.driver.get(url=url)
            log.info(f'成功访问页面：{url}')
        except Exception as e:
            self.page_screenshot('访问页面失败')
            log.error(f'访问页面{url}失败')
            log.exception(e)
            raise e

    # 鼠标点击
    def mouse_click(self, element):
        try:
            self.driver.find_element(*element).click()
            log.info('鼠标点击正常')
        except Exception as e:
            self.page_screenshot('鼠标点击失败')
            log.error('鼠标点击失败')
            log.exception(e)
            raise e

    # 滑动到元素当前位置并点击
    def mouse_slide_click(self, element):
        try:
            el = self.driver.find_element(*element)
            el.location_once_scrolled_into_view
            el.click()
            log.info('鼠标点击正常')
        except Exception as e:
            self.page_screenshot('鼠标点击失败')
            log.error('鼠标点击失败')
            log.exception(e)
            raise e

    # 鼠标双击
    def mouse_double_click(self, element):
        try:
            el = self.driver.find_element(*element)
            self.action.double_click(el).perform()
            log.info('鼠标双击击正常')
        except Exception as e:
            self.page_screenshot('鼠标双击失败')
            log.error('鼠标双击失败')
            log.exception(e)
            raise e

    # 鼠标拖动
    def mouse_drag(self, start_position, end_position):
        try:
            el1 = self.driver.find_element(*start_position)
            el2 = self.driver.find_element(*end_position)
            self.action.drag_and_drop(el1, el2).perform()
            log.info('鼠标拖动正常')
        except Exception as e:
            self.page_screenshot('鼠标拖动失败')
            log.error('鼠标拖动失败')
            log.exception(e)
            raise e

    # 页面滚动条
    def browser_scroll_bar(self, start, end):
        try:
            js_str = f"window.scrollTo({start}, {end})"
            self.driver.execute_script(js_str)
            log.info('页面滚动正常')
        except Exception as e:
            self.page_screenshot('页面滚动失败')
            log.error('页面滚动失败')
            log.exception(e)
            raise e

    # 输入
    def input_content(self, element, text):
        try:
            self.driver.find_element(*element).send_keys(text)
            log.info('输入正常')
        except Exception as e:
            self.page_screenshot('输入失败')
            log.error('输入失败')
            log.exception(e)
            raise e

    # 鼠标悬停
    def mouse_hover(self, element):
        try:
            el = self.driver.find_element(*element)
            self.action.move_to_element(el).perform()
        except Exception as e:
            self.page_screenshot('鼠标悬停失败')
            log.error('鼠标悬停失败')
            log.exception(e)
            raise e

    # 浏览器窗口切换
    def window_switching(self, index):
        try:
            keys = self.driver.window_handles
            self.driver.switch_to.window(keys[index])
        except Exception as e:
            self.page_screenshot('浏览器窗口切换失败')
            log.error('浏览器窗口切换失败')
            log.exception(e)
            raise e

    # alert弹窗切换
    def alert_switching(self):
        try:
            self.driver.switch_to.alert.accept()
        except Exception as e:
            self.page_screenshot('alert弹窗切换失败')
            log.error('alert弹窗切换失败')
            log.exception(e)
            raise e

    # 设置属性
    def set_property(self, element, attribute_name, attribute_value):
        try:
            el = self.driver.find_element(*element)
            self.driver.execute_script(f"arguments[0].{attribute_name} = {attribute_value}", el)
        except Exception as e:
            self.page_screenshot('设置属性失败')
            log.error('设置属性失败')
            log.exception(e)
            raise e

    # 文件上传input元素
    def file_upload(self, element, file_url):
        try:
            self.driver.find_element(*element).send_keys(file_url)
        except Exception as e:
            self.page_screenshot('文件上传失败')
            log.error('文件上传失败')
            log.exception(e)
            raise e

    # 键盘回车操作
    def keys_enter(self, element):
        try:
            self.driver.find_element(*element).send_keys(Keys.ENTER)
        except Exception as e:
            self.page_screenshot('键盘回车操作失败')
            log.error('键盘回车操作失败')
            log.exception(e)
            raise e

    # 元素添加显示等待(可以被点击)
    def wait_clickable(self, element):
        try:
            wait = WebDriverWait(self.driver, 10)
            el = wait.until(expected_conditions.element_to_be_clickable(element))
            return el
        except Exception as e:
            self.page_screenshot('元素添加显示等待失败')
            log.error('元素添加显示等待失败')
            log.exception(e)
            raise e

    # 元素添加显示等待(加载完成)
    def wait_presence(self, element):
        try:
            wait = WebDriverWait(self.driver, 10)
            el = wait.until(expected_conditions.presence_of_element_located(element))
            return el
        except Exception as e:
            self.page_screenshot('元素添加显示等待失败')
            log.error('元素添加显示等待失败')
            log.exception(e)
            raise e

    # 元素添加显示等待(元素可以被看见)
    def wait_visibility(self, element):
        try:
            wait = WebDriverWait(self.driver, 10)
            el = wait.until(expected_conditions.visibility_of_element_located(element))
            return el
        except Exception as e:
            self.page_screenshot('元素添加显示等待失败')
            log.error('元素添加显示等待失败')
            log.exception(e)
            raise e

    # 断言文本
    def assert_element_text_equal(self, element, expected):
        try:
            el = self.driver.find_element(*element)
            assert el.text == expected
        except Exception as e:
            self.page_screenshot('断言文本失败')
            log.error('断言文本失败')
            log.exception(e)
            raise e

    # 数据库断言（通过手机号查询是否注册成功）
    def assert_mysql_register(self, phone):
        try:
            my_sql = HandleMySql()
            str_sql = f"SELECT user_name FROM tz_user WHERE user_mobile = '{phone}'"
            data = my_sql.get_data(str_sql)
            my_sql.close_mysql()
            assert isinstance(data, tuple)
        except Exception as e:
            self.page_screenshot('数据库断言（通过手机号查询是否注册成功）失败')
            log.error('数据库断言（通过手机号查询是否注册成功）失败')
            log.exception(e)
            raise e

    # 断言某个元素的属性
    def assert_element_attr_equal(self, element, attr_name, expected):
        try:
            el = self.driver.find_element(*element)
            attr_value = el.get_attribute(attr_name)
            assert attr_value == expected
        except Exception as e:
            self.page_screenshot('断言某个元素的属性失败')
            log.error('断言某个元素的属性失败')
            log.exception(e)
            raise e

    # 断言某个元素是否存在
    def assert_element_whether_it_exists(self, element):
        try:
            assert self.driver.find_element(*element)
        except Exception as e:
            self.page_screenshot('断言元素是否存在失败')
            log.error('断言元素是否存在失败')
            log.exception(e)
            raise e

    # 断言通过跳转路径
    def assert_url(self, expected_url):
        try:
            url = self.get_page_url()
            assert url == expected_url
        except Exception as e:
            self.page_screenshot('断言失败')
            log.error('断言失败')
            log.exception(e)
            raise e

    # 获取当前页面路径
    def get_page_url(self):
        try:
            return self.driver.current_url
        except Exception as e:
            log.error('获取当前页面路径失败')
            log.exception(e)
            raise e

    # 生成手机号
    def get_phone(self):
        try:
            fk = Faker(locale='zh_CN')
            return fk.phone_number()
        except Exception as e:
            log.error('生成手机号失败')
            log.exception(e)
            raise e

    # 生成还未注册的手机号
    def phone_checking(self):
        try:
            my_sql = HandleMySql()
            while True:
                phone = self.get_phone()
                str_sql = f"SELECT user_name FROM tz_user WHERE user_mobile = '{phone}'"
                data = my_sql.get_data(str_sql)
                if isinstance(data, tuple):
                    break
            my_sql.close_mysql()
            return phone
        except Exception as e:
            log.error('生成还未注册的手机号失败')
            log.exception(e)
            raise e

    # 通过手机号获取验证码
    def get_check_code(self, phone):
        try:
            my_sql = HandleMySql()
            str_sql = f"SELECT mobile_code as code FROM tz_sms_log WHERE user_phone = '{phone}' ORDER BY rec_date DESC"
            code = my_sql.get_data(str_sql)
            my_sql.close_mysql()
            return code[0]['code']
        except Exception as e:
            log.error('通过手机号获取验证码失败')
            log.exception(e)
            raise e


if __name__ == '__main__':
    cl = Browser(webdriver.Chrome)
    print(cl.mouse_click(('xpath', "//input[@placeholder='请输入商品名称']")))