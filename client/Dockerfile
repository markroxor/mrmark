FROM python:3
LABEL maintainer="Mohit Rathore"

RUN apt-get update && \
  apt-get install -y supervisor python3-xlib python3-tk xvfb x11-xserver-utils
RUN \
  Xvfb :1 -screen 0 1366x768x16 &> xvfb.log && \
  export DISPLAY=:1.0 && \
  touch ~/.Xauthority && \
  pip3 install image && \
  pip3 install python3-xlib && \
  pip3 install pyautogui

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY . ./
RUN pip install -r requirements.txt
CMD xhost + && python app.py

