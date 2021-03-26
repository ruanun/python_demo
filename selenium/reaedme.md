## 各个浏览器driver下载地址：
官方文档：https://www.selenium.dev/documentation/zh-cn/getting_started_with_webdriver/browsers/ 

* ChromeDriver  下载地址： https://sites.google.com/a/chromium.org/chromedriver/
* Firefox geckodriver 下载地址：https://github.com/mozilla/geckodriver/
* Edge 下载地址： https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
* Opera 下载地址：https://github.com/operasoftware/operachromiumdriver/
* Safari 下载地址：https://webkit.org/blog/6900/webdriver-support-in-safari-10/


python-docker-selenium 镜像：
https://github.com/joyzoursky/docker-python-chromedriver


## selenium 官方的远程webdriver服务 docker 镜像：
地址：https://github.com/SeleniumHQ/docker-selenium

docker 启动服务：

```shell script
# 自带vnc 可远程vnc链接查看。vnc链接密码:
docker run -d --rm --name scd -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug
# 不带 vnc 
docker run -d --rm --name scd -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome

``` 

python代码中链接：
```python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

time.sleep(5)
driver = webdriver.Remote(
    command_executor="http://chrome:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME
)
driver.get("http://www.baidu.com")
print(driver.title)
driver.close()
```

