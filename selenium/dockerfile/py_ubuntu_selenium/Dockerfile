FROM ubuntu

MAINTAINER ruanun

ENV TZ=Asia/Shanghai

# install tool
RUN apt-get update && apt-get install wget unzip python3 python3-pip gnupg2 curl -y && pip3 install selenium

# 设置时区
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && apt-get install tzdata -y


# 安装 Chrome
#RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
#     && apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN wget -q -O -  https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get -y install google-chrome-stable

# 安装 chromedriver
RUN wget -O chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip chromedriver.zip -d /usr/local/bin/

RUN apt-get clean && apt-get autoclean
