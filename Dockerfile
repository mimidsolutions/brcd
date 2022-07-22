FROM amazonlinux:2


RUN amazon-linux-extras install epel -y && \
    yum install -y zbar && \
    yum install ffmpeg libsm6 libxext6  -y && \ 
    yum install -y opencv-python && \
    mkdir -p /app

WORKDIR /app
COPY . .    
RUN pip3 install -r requirements.txt

CMD ["gunicorn", "--access-logfile=-", "--bind", "0.0.0.0:8080", "-w", "2", "fe_api:app"]