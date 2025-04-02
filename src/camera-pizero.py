#!/usr/bin/python3

from gpiozero import Button
from libcamera import Transform
from picamera2 import Picamera2, Preview, MappedArray
from glob import glob
import cv2

button = Button(13)
frame = 1

def apply_txt(request):
    global frame
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, "%04d" % frame, (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

def main():
    global frame
    picam2 = Picamera2()
    picam2.start_preview(Preview.DRM, width=480, height=320)
    preview_config = picam2.create_preview_configuration({"format": "XRGB8888","size": (480, 320)}, transform=Transform(hflip=1, vflip=1), queue=False)
    capture_config = picam2.create_still_configuration(transform=Transform(hflip=1, vflip=1))
    picam2.configure(preview_config)
    picam2.start()
    try:
        frame = int(sorted(glob("*.jpg"))[-1][:-4]) + 1
    except:
        frame = 1
    print(frame)
    picam2.post_callback = apply_txt
    while True:
        button.wait_for_press()
        picam2.switch_mode_and_capture_file(capture_config, "%04d.jpg" % frame)
        print("saved %04d.jpg" % frame)
        frame += 1

if __name__ == "__main__":
    main()