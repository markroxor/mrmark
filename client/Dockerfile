FROM python:3
RUN apt-get update
RUN apt-get install -y supervisor
RUN apt-get install -y python3-xlib python3-tk xvfb
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
CMD ls
CMD ["/usr/bin/supervisord"]

