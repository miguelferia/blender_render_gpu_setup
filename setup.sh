#! /bin/bash

wget http://us.download.nvidia.com/tesla/418.87/nvidia-driver-local-repo-ubuntu1804-418.87.01_1.0-1_amd64.deb
dpkg -i nvidia-driver-local-repo-ubuntu1804-418.87.01_1.0-1_amd64.deb
apt-key add /var/nvidia-driver-local-repo-418.87.01/7fa2af80.pub
dpkg -i nvidia-driver-local-repo-ubuntu1804-418.87.01_1.0-1_amd64.deb

apt update
apt install cuda-drivers -y

snap install blender --classic
apt install libgl1-mesa-glx libxi6 libxrender1 nvtop -y
