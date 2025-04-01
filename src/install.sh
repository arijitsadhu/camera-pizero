#!/bin/bash

apt-get update
apt-get install --no-install-recommends -y python3-picamera2
sed -i -e 's/\"XB24\"/\"XR24\"/' /usr/lib/python3/dist-packages/picamera2/previews/drm_preview.py
sed -i -e 's/dtoverlay=vc4-kms-v3d/dtoverlay=vc4-kms-v3d,nohdmi/' /boot/firmware/config.txt
echo "dtoverlay=piscreen,speed=16000000,rotate=180,drm" >> /boot/firmware/config.txt
mkdir /DCIM
chmod a+rw /DCIM
cp camera-pizero.py /usr/local/bin/
cp camera-pizero.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable camera-pizero.service
