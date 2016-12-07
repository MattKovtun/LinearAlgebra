import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def grayscale(filename):
    img = mpimg.imread(filename)
    return np.dot(img[...,:3], [0.299, 0.587, 0.114])


gray = grayscale("face.png")
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.show()