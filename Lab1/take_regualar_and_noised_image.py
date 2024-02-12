import cv2
import numpy as np
from matplotlib import pyplot as plt
from picamera2 import Picamera2, Preview
from libcamera import controls

picam2 = Picamera2()

config = picam2.create_preview_configuration()

picam2.configure(config) 

picam2.start_preview(Preview.QTGL)
picam2.start()


# In interactive mode:

"""
Create still config:

still_conf = picam2.create_still_configuration()

Apply some corrections, e.g:

picam2.set_controls({ "Brightness": 0.125 })
or
picam2.set_controls({ "NoiseReductionMode": controls.draft.NoiseReductionModeEnum.HighQuality })
or
picam2.set_controls({ "AwbMode": controls.AwbModeEnum.Fluorescent })

Take image:

picam2.switch_mode_and_capture_file(still_conf, 'regular.jpg')

Add noise:

picam2.set_controls({ "NoiseReductionMode": controls.draft.NoiseReductionModeEnum.Off })
or
picam2.set_controls({ "AnalogueGain": 89.0 })

Take image:

picam2.switch_mode_and_capture_file(still_conf, 'noised.jpg')

"""