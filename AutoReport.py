from selenium import webdriver
from time import sleep
import logging

from selenium.webdriver.edge.options import Options

import encode


from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By


def auto_report(data):
    print("processing...")
    userName = data.get("userName")
    passwd = data.get("passwd")
    nickName = data.get("nickName")
    location_input = data.get("location")
    nickName = '[' + nickName + ']'
    options = Options()
    options.add_argument("headless")
    path = "./edgedriver_linux64/msedgedriver"
    bor = webdriver.Edge(path, options=options)
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
        
        if location_input is not None:
            location_encode = encode.parse_code(location_input)
            bor.get("http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx?"+location_encode)
            loc = bor.find_element(by=By.XPATH, value="/html/body/form/div[15]/div/input")
            if '✰' in location_input:
                location_input = location_input.replace('✰', ' ')
            loc.send_keys(location_input)
            notInSchool = bor.find_element(by=By.XPATH, value="/html/body/form/div[12]/div[4]/input")
            notInSchool.click()
        if location_input is None:
            # 婺城区
            bor.get("http://zyt.zjnu.edu.cn/H5/ZJSFDX/FillIn.aspx?address=%E6%B5%99%E6%B1%9F%E7%9C%81%E2%9C%B0%E9%87%91%E5%8D%8E%E5%B8%82%E2%9C%B0%E5%A9%BA%E5%9F%8E%E5%8C%BA")
            location = bor.find_element(by=By.XPATH, value="/html/body/form/div[12]/div[1]/input")
            location.click()

        greenQr = bor.find_element(by=By.XPATH, value="/html/body/form/div[9]/div[1]/input")
        greenQr.click()

        i_know = bor.find_element(by=By.XPATH, value="/html/body/form/div[51]/div/input")
        i_know.click()
        sleep(6)

        submit = bor.find_element(by=By.XPATH, value="/html/body/form/div[52]/div/a")
        submit.click()

    except NoSuchElementException as nos:
        logging.info(nickName + " error,element has changed" + str(nos))
    except ElementNotInteractableException as ele:
        logging.info(nickName + userName + " already report!" + str(ele))
    except Exception as e:
        logging.info(nickName + str(e))
    finally:
        # 谨防搞崩网站
        sleep(3)
        bor.close()
