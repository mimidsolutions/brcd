#!/bin/bash
sudo amazon-linux-extras install epel -y
sudo yum install -y zbar
pip install -r requirements.txt