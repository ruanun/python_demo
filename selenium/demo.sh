docker run -it --rm --name my-running-script -v /root:/usr/src/myapp -v /dev/shm:/dev/shm -w /usr/src/myapp ruanun/python-docker-selenium:3.8 python3 demo.py
