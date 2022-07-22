#!/bin/bash
sudo amazon-linux-extras install epel -y
sudo yum install -y zbar
sudo yum install -y opencv-python
pip3 install -r requirements.txt
