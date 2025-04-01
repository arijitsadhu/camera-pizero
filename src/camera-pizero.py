#!/usr/bin/python3

from gpiozero import Button
from libcamera import Transform
from picamera2 import Picamera2, Preview
from glob import glob

button = Button(13)

def main():    
    picam2 = Picamera2()
    picam2.start_preview(Preview.DRM, width=480, height=320)
    preview_config = picam2.create_preview_configuration({"format": "XRGB8888","size": (480, 320)}, transform=Transform(hflip=1, vflip=1))
    capture_config = picam2.create_still_configuration(transform=Transform(hflip=1, vflip=1))
    picam2.configure(preview_config)
    picam2.start()
    try:
        frame = int(sorted(glob("*.jpg"))[-1][:-4]) + 1
    except:
        frame = 1
    print(frame)
    while True:
        button.wait_for_press()
        picam2.switch_mode_and_capture_file(capture_config, "%03d.jpg" % frame)
        print("%03d.jpg" % frame)
        frame += 1

if __name__ == "__main__":
    main()