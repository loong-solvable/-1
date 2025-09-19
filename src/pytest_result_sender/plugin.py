from datetime import datetime


def pytest_configure():

    # 配置加载完毕后执行，测试用例执行之前

    print(f"{datetime.now()} pytest开始执行了")


def pytest_unconfigure():
    # 配置卸载之后，测试执行后。执行
    print(f"{datetime.now()} pytest结束执行")
