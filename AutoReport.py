from selenium import webdriver
from time import sleep
import logging

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By


def auto_report(data):
    userName = data.get("userName")
    passwd = data.get("passwd")
    nickName = data.get("nickName")
    # logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
    #                     filename='report.log',
    #                     filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
    #                     # a是追加模式，默认如果不写的话，就是追加模式
    #                     format=
    #                     '%(asctime)s - %(levelname)s: %(message)s'
    #                     # 日志格式
    #                     )
    nickName = '[' + nickName + ']'
    bor = webdriver.Edge()
    bor.get("http://zyt.zjnu.edu.cn/H5/Login.aspx?op=phone_html5")
    logging.info("=============================" + nickName + " processing" + "=================================")

    try:

        # 账号密码
        userText = bor.find_element(by=By.XPATH, value="/html/body/form/div[3]/div[4]/input")
        userText.send_keys(userName)

        passwdText = bor.find_element(by=By.XPATH, value="/html/body/form/div[3]/div[5]/input")
        passwdText.send_keys(passwd)

        # 登录
        login = bor.find_element(by=By.XPATH, value="/html/body/form/div[3]/div[7]/input")
        login.click()
        logging.info(nickName + " login now !")

        # 信息填报
        report = bor.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/ul/li[2]/a")
        report.click()

        # 点击进入详情页
        report_start = bor.find_element(by=By.XPATH, value="/html/body/form/div[4]/button[1]")
        report_start.click()
        # 婺城区
        bor.get("http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx?address=%E6%B5%99%E6%B1%9F%E7%9C%81%E2%9C%B0%E9%87%91%E5%8D%8E%E5%B8%82%E2%9C%B0%E5%A9%BA%E5%9F%8E%E5%8C%BA")

        location = bor.find_element(by=By.XPATH, value="/html/body/form/div[48]/div[1]/input")
        location.click()

        i_know = bor.find_element(by=By.XPATH, value="/html/body/form/div[54]/div/input")
        i_know.click()

        sleep(6)

        submit = bor.find_element(by=By.XPATH, value="/html/body/form/div[55]/div/a")
        submit.click()
    except NoSuchElementException:
        logging.info(nickName + " error,element has changed")
    except ElementNotInteractableException:
        logging.info(nickName + userName + " already report!")
    except Exception as e:
        logging.info(nickName + str(e))
    finally:
        # 谨防搞崩网站
        sleep(3)
        bor.close()
