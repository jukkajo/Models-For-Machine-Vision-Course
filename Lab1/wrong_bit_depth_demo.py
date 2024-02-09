from picamera2 import Picamera2, MappedArray, Preview
import numpy as np

picam2 = Picamera2()
width = 800
height = 600
slice_width = round(width / 5)

def apply_shift(request):
    with MappedArray(request, "main") as m:

        # Slice and shift each slice different amount
        slice_a = m.array[:,0:slice_width] << 2
        slice_b = m.array[:,slice_width:slice_width*2] << 1
        slice_c = m.array[:,slice_width*2:slice_width*3]
        slice_d = m.array[:,slice_width*3:slice_width*4] >> 1
        slice_e = m.array[:,slice_width*4:width] >> 2

        # Concatenate slices and write back to the stream
        m.array[:] = np.concatenate((slice_a, slice_b, slice_c, slice_d, slice_e), axis=1)

        # Remove pointer to the original array
        del slice_c

# Lower resultion (to not kill the CPU)
config = picam2.create_preview_configuration(
    main={"size": (width, height)},
    display="main"
)
picam2.configure(config)

picam2.pre_callback = apply_shift
picam2.start_preview(Preview.QTGL, x=100, y=100, width=width, height=height)
picam2.start()
