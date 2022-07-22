#!/bin/bash
sudo amazon-linux-extras install epel -y
sudo yum install -y zbar
sudo yum install ffmpeg libsm6 libxext6  -y
sudo yum install -y opencv-python
pip3 install -r requirements.txt


yum localinstall -y --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm
sudo su -
cd /usr/local/bin
mkdir ffmpeg && cd ffmpeg
cd ffmpeg
wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz
tar -zxvf ffmpeg-release-amd64-static.tar.xz
