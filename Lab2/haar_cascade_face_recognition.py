from picamera2 import Picamera2, MappedArray
import cv2

face_detector = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

# Map rectangles from lower resolution stream to preview (main) stream
def draw_faces(request):
  with MappedArray(request, "main") as m:
    for f in faces:
      (x, y, w, h) = [c * n // d for c, n, d in zip(f, (w0, h0) * 2, (w1, h1) * 2)]
      cv2.rectangle(m.array, (x, y), (x + w, y + h), (0, 255, 0, 0))

# Start and configure camera with low resolution and main streams
picam2 = Picamera2()
config = picam2.create_preview_configuration(
  main={"size": (640, 480)},
  lores={"size": (320, 240), "format": "YUV420"}
)
picam2.configure(config)

# In theory, picamera might change the resolution if it cannot be efficietly supported
# So we check what the actual stream resolutions are
(w0, h0) = picam2.stream_configuration("main")["size"]
(w1, h1) = picam2.stream_configuration("lores")["size"]

# Init stuff
faces = []
picam2.post_callback = draw_faces

# Start capturing and preview window
picam2.start(show_preview=True)

# Start face recognition loop
array = None
while True:
  array = picam2.capture_array("lores")
  grey = array[0:h1,:]
  faces = face_detector.detectMultiScale(grey, 1.1, 3)
