### 2022/01/22 更新内容：自定义定位设置、不在校选项设置

### 2021/12/19 更新内容：定位将默认在学校本部校区

# auto_report_zyt
战役通打卡(gitee地址：https://gitee.com/ZJNUWL1024/auto_report_zyt)

- 需要提前edge webdrive
- 需要自己改动run.bat和start.bat的路径（相信聪明的你肯定能够搞定）

## AutoReport.py

利用Selenium模拟人为点击填写上报内容

## main.py

使用线程池提高性能、日志输出到当前目录的report.log中

## run.bat

使用windows的schtasks设置每天定时自动执行

## start.bat

执行py文件
