# 基础镜像 https://github.com/ConSol/docker-headless-vnc-container
FROM consol/ubuntu-xfce-vnc

# Switch to root user to install additional software
USER 0

RUN apt-get update && apt-get upgrade -y && apt-get install python3-pip unzip curl wget software-properties-common -y

RUN pip3 install selenium

RUN wget -O chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip chromedriver.zip -d /usr/local/bin/

## switch back to default user
#USER 1000


