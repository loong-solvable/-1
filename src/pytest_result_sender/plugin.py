from datetime import datetime,timedelta
import pytest
import requests

from requests import session

data = {
    "failed": 0,
    "passed": 0,
}


def pytest_runtest_logreport(report:pytest.TestReport):
    #print(report)
    if report.when == 'call':
        print("本次用例的执行结果： ",report.outcome)
        data[report.outcome] += 1

def pytest_collection_finish(session: pytest.Session):
    # 用例加载完成后执行。包含了全部的用例
    data['total'] = len(session.items)
    print("用例的总数: ",data['total'])


def pytest_configure():

    # 配置加载完毕后执行，测试用例执行之前
    data['start_time'] = datetime.now()
    print(f"{datetime.now()} pytest开始执行了")


def pytest_unconfigure():
    # 配置卸载之后，测试执行后。执行

    data['end_time'] = datetime.now()

    print(f"{datetime.now()} pytest结束执行")

    data['duration'] = data['end_time'] - data['start_time']

    data['pass_rate'] = data['passed'] / data['total'] * 100
    data['pass_rate'] = f"{data['pass_rate']:.2f}%"


   # # print(data)
   #  assert timedelta(seconds=3) > data['duration'] >= timedelta(seconds=2.5)
   #  assert data['total'] == 3
   #  assert data['passed'] == 2
   #  assert data['failed'] == 1
   #  print(data['pass_rate'])
   #  assert data['pass_rate'] == '66.67%'



url = 'https://work.weixin.qq.com/wework_admin/common/openBotProfile/24b1b5ff140ddffd4350b45cc06a2ca3af'

content = f"""
   pytest自动化测试结果
   测试时间：{data['end_time']} <br/>
   用例数量：{data['total']}<br/>
   执行时长：{data['duration']}s <br/>
   测试通过：<font color='green'>{data['passed']}</font><br/>
   测试失败：<font color='red'>{data['failed']}</font><br/>
   测试通过率：{data['pass_rate']}<br/>
   测试报告地址：http：//baidu.com
   """

requests.post(url,
              json={

              })