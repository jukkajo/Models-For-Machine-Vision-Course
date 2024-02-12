import cv2
import numpy as np
from matplotlib import pyplot as plt
from picamera2 import Picamera2, Preview
from libcamera import controls
import scipy.ndimage
from PIL import Image

#Load and denoise noised:

noised = Image.open('noised.jpg').convert('L')

regular = Image.open('regular.jpg').convert('L')

#Optional additional noise: grayscaled = grayscaled + 0.2 * np.random.normal(size=grayscaled.shape)

denoised = scipy.ndimage.median_filter(noised, size=3)

#Display:
fig, axes = plt.subplots(1,3, figsize=(10,4))

axes[0].imshow(regular, cmap="gray")
axes[0].set_title("Regular")
axes[0].axis("off")

axes[1].imshow(noised, cmap="gray")
axes[1].set_title("Noised")
axes[1].axis("off")

axes[2].imshow(denoised, cmap="gray")
axes[2].set_title("Denoised")
axes[2].axis("off")

# Remember to save figure via plot window
plt.show()