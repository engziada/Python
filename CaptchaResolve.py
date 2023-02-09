import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from scipy.signal import convolve2d

# get numpy array from img
image = Image.open("captcha-img.png").convert("L")
img = np.array(image)

# blur img via convolution
blur_size = 3
blur_repeat = 6
blur_kernel = np.ones((blur_size, blur_size))
for _ in range(blur_repeat):
    img = convolve2d(img, blur_kernel)

# threshold and crop
remaining_img = img > np.median(img)
border = blur_size*blur_repeat
plt.imshow(remaining_img[border:-border+1, border:-border+1])
plt.show()
