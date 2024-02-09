from picamera2 import Picamera2, Preview
from libcamera import controls

picam2 = Picamera2()

config = picam2.create_preview_configuration()

picam2.configure(config) 

picam2.start_preview(Preview.QTGL)
picam2.start()

# In interactive mode:

"""

Config for still images:
still_conf = picam2.create_still_configuration()

Return adjustable camera parameters:
picam2.camera_controls

Param value change example:
picam2.set_controls({ "ControlName": value, "AnotherControl": value2 })

Validate succesful changes:
picam2.capture_metadata()

Change to above initialized configuration and take still image:
picam2.switch_mode_and_capture_file(still_conf, 'img.jpg')

"""
