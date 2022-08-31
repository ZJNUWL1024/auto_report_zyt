from multiprocessing.pool import ThreadPool

from AutoReport import auto_report
import logging
import time


def process(data_arr):
    pool = ThreadPool()
    pool.map(auto_report, data_arr)
    pool.close()
    pool.join()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                        filename='./report.log',
                        filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format=
                        '%(asctime)s - %(levelname)s: %(message)s'
                        # 日志格式
                        )
    start = time.time()
    datas = [
        {
            'userName': 'xxx',
            'passwd': 'xxx',
            'nickName': 'xx',
            'location': "浙江省✰杭州市✰拱墅区"
        },
        {
            'userName': 'xxx',
            'passwd': 'xx',
            'nickName': 'WJ',
        },
        {
            'userName': 'xxx',
            'passwd': 'xxx',
            'nickName': 'xx',
            'location': "浙江省✰嘉兴市✰南湖区"
        }
    ]
    process(datas)
    end = time.time()
    logging.info("process time : " + str(int(end-start)) + 's')


