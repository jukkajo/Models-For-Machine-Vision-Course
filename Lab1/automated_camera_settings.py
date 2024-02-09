from picamera2 import Picamera2, MappedArray, CompletedRequest
import cv2

picam2 = Picamera2()
colour = (255, 255, 255)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 0.5
thickness = 1

def apply_timestamp(request: CompletedRequest):
    meta = request.get_metadata()
    exp_str = f"Exposure: {meta['ExposureTime'] / 1000} ms"
    a_gain_str = f"Analogue gain: {round(meta['AnalogueGain'], 2)}"
    d_gain_str = f"Digital gain: {round(meta['DigitalGain'], 2)}"
    color_temp_str = f"Color temperature: {meta['ColourTemperature']}"
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, exp_str, (15, 30), font, scale, colour, thickness)
        cv2.putText(m.array, a_gain_str, (15, 50), font, scale, colour, thickness)
        cv2.putText(m.array, d_gain_str, (15, 70), font, scale, colour, thickness)
        cv2.putText(m.array, color_temp_str, (15, 90), font, scale, colour, thickness)

picam2.pre_callback = apply_timestamp
picam2.start(show_preview=True)

# In interactive mode:

"""

AeEnable allows the AEC/AGC algorithm to be turned on and off. When if is off, there will be no
automatic updates to the camera’s gain or exposure settings:

picam2.set_controls({"AeEnable" : True})
--------------------------------------------------------------------------------------------------
AwbEnable turns the auto white balance (AWB) algorithm on or off. When it is off, there will be no
automatic updates to the colour gains:

picam2.set_controls({"AwbEnable" : False})
--------------------------------------------------------------------------------------------------
Brightness adjusts the image brightness where -1.0 is very dark, 1.0 is very bright, and 0.0 is the
default "normal" brightness.:

picam2.set_controls({"Brightness" : 0.3})

"""
