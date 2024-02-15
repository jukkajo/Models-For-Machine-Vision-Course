from picamera2 import Picamera2
from PIL import Image
import numpy as np
from matplotlib import pyplot

picam2 = Picamera2()
conf = picam2.create_still_configuration()
picam2.start(show_preview=True)

picam2.set_controls({
    "AeEnable": False,
    "ExposureTime": 80000,
    "AnalogueGain": 2.0
})

# Take picture 1
print("Adjust aperture so that picture is as bright as possible without burns.")
input("Enter to capture flat field")
picam2.switch_mode_and_capture_file(conf, "flat.jpg")

# Take picture 2
print("Place cat in front of the camera")
input("Enter to capture image")
picam2.switch_mode_and_capture_file(conf, "image.jpg")

# Calculate final image
flat = np.array(Image.open("flat.jpg"), dtype=np.uint8)
img = np.array(Image.open("image.jpg"), dtype=np.uint8)

result = img / flat # Float 64, roughly between 0.0 - 1.0 (can be over 1)

pyplot.imsave("result.jpg", np.clip(result, 0., 1.))

# Alternative way to save using PIL
# result_im = Image.fromarray(np.uint8(np.clip(result, 0., 1.) *255))
# result_im.save("result.jpg")
