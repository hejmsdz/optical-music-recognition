# import cv2
# import IPython

# def imshow(img):
#     _,ret = cv2.imencode('.png', img) 
#     i = IPython.display.Image(data=ret)
#     IPython.display.display(i)

import cv2
from  matplotlib import pyplot as plt

def imshow(im):
    plt.figure(figsize=(12, 12))
    if len(im.shape) == 3:
        plt.imshow(im)
    else:
        plt.imshow(im, cmap='gray')
    plt.show()
