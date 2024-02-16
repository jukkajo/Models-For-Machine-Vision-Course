from picamera2 import Picamera2
from pprint import pprint
from libcamera import controls

picam2 = Picamera2()
conf = picam2.create_still_configuration()
picam2.start(show_preview=True)

picam2.set_controls({ "AeMeteringMode": controls.AeMeteringModeEnum.Spot })


# In interactive mode

#picam2.set_controls({ "ExposureTime": 1000 })

#picam2.switch_mode_and_capture_file(conf, "kuva-1.jpg")exit
